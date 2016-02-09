#!/usr/bin/env python2

from json import load
from urlparse import urlparse

def process_add(command, arg, dep):
    src,dst = arg.split()
    urlparts = urlparse(src)
    if not urlparts.scheme or urlparts.scheme == 'file':
        src = "lib/%s/%s" % (dep,urlparts.path)
        arg = "%s %s" % (src,dst)
    return command,arg

command_dict = {
    "repo_update": ["RUN apt-get -y update", None],
    "repo_add"   : ["RUN add-apt-repository -y", None],
    "install"    : ["RUN apt-get install -y --force-yes --no-install-recommends", None],
    "purge"      : ["RUN apt-get purge -y --force-yes", None],
    "add"        : ["add", process_add]
}

def load_dep(dep, commands=[], expose_ports=[], entry_points=[]):
    path = "lib/%s.json" % dep
    json_data = load(open(path, "rb"))
    depends   = json_data.get('depends', [])
    commands.append("#%s.json" % dep)
    for dep in depends:
        load_dep(dep, commands)
    for command in json_data['commands']:
        try:
            command,arg = command
        except ValueError:
            arg = ""
        command,fnc = command_dict.get(command, ["RUN %s" % command, None])
        try:
            command,arg = fnc(command,arg,dep)
        except TypeError:
            pass
        command = "%s %s" % (command, arg)
        commands.append(command)
    commands.append("#--")

    expose = json_data.get('expose', [])
    expose_ports.extend(expose)

    entry_point = json_data.get("entrypoint", [])
    if entry_point:
        entry_points.append(entry_point)

    return commands,expose_ports,entry_points

def load_json(json_path, dockerfile=None):
    import json
    data = load(open(json_path, "rb"))
    maintainer = data.get('maintainer')
    if maintainer:
        maintainer = "Maintainer %s" % maintainer
    if not dockerfile:
        dockerfile = [
            "FROM ubuntu:14.04",
            maintainer,
            "ENV DEBIAN_FRONTEND noninteractive",
            "ENV HOME /root",
            "RUN apt-get update",
            "RUN apt-get install -y --force-yes --no-install-recommends software-properties-common",
        ]

    sub_commands = []
    expose_ports = []
    entry_points = []
    for lib in data.get('libs', []):
        sub_commands,expose_ports,entry_points = load_dep(lib)
    dockerfile.extend(sub_commands)
    dockerfile.extend([
        "RUN apt-get purge software-properties-common -y --force-yes",
        "RUN apt-get -y autoclean",
        "RUN apt-get -y autoremove",
        "RUN rm -rf /var/lib/apt/lists/*",
    ])
    if expose_ports:
        dockerfile.append("EXPOSE %s" % " ".join(expose_ports))
    if entry_points:
        entry_point = entry_points[-1]
        dockerfile.append("ENRTYPOINT %s" % json.dumps(entry_point))
    
    dockerfile = "\n".join(dockerfile)
    return dockerfile

if __name__=="__main__":
    from sys import argv
    from getopt import getopt

    json_file = None
    outputfile = None

    opts,args = getopt(argv[1:], "f:o:", ["file=", "outputfile="])
    for opt,arg in opts:
        if opt in ['-f', '--file']:
            json_file = arg
        elif opt in ['-o', '--outputfile']:
            outputfile = arg
    if not json_file:
        print "Input file needed, -f, --file"
        exit(1)
    out_json_file = load_json(json_file)
    if outputfile:
        out_file = open(outputfile, "wb")
        out_file.write(out_json_file)
    else:
        print out_json_file
