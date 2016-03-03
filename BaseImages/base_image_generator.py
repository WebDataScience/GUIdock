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
    "repo_add"   : ["RUN add-apt-repository -y", lambda command,arg,dep: (command,"'%s'" % arg)],
    "install"    : ["RUN apt-get install -y --force-yes --no-install-recommends", None],
    "purge"      : ["RUN apt-get purge -y --force-yes", None],
    "add"        : ["add", process_add],
    "copy"       : ["copy", process_add]
}

def load_dep(dep, commands=[], expose_ports=[], entry_points=[], scripts=[], env=[], workdir=[], contributors=[]):
    path = "lib/%s.json" % dep
    try:
        json_data = load(open(path, "rb"))
    except Exception as e:
        from sys import exit
        print("Failed to import %s: %s" % (dep, e))
        exit(1)
    depends   = json_data.get('depends', [])
    commands.append("#%s.json" % dep)
    for _dep in depends:
        load_dep(_dep, commands, scripts=scripts, env=env)
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

    for _env in json_data.get("env", []):
        env.append(_env)

    entry_point = json_data.get("entrypoint", [])
    if entry_point:
        entry_points.append(entry_point)
    try:
        script,script_opts = json_data.get("script")
    except ValueError:
        script = json_data.get("script")
        script_opts = {'remove': True}
    except TypeError:
        script = None
    if script:
        from uuid import uuid4
        # Generate uuid4 name for first time setup script
        file_name = str(uuid4())
        arg = "%s /%s" % (script,file_name)
        command,arg = process_add("add", arg, dep)
        command = "%s %s" % (command,arg)
        commands.append(command)
        command_str = "/%s" % file_name
        scripts.append("chmod +x %s" % command_str)
        scripts.append(command_str)
        if script_opts['remove']:
            scripts.append("rm -rf %s" % command_str)
    workdir = workdir + json_data.get('workdir', [])
    contributors = contributors+json_data.get('maintainer', [])

    return commands,expose_ports,entry_points,scripts,env,workdir,contributors

def load_json(json_path, dockerfile=None):
    import json
    data = load(open(json_path, "rb"))
    maintainer = data.get('maintainer')
    if maintainer:
        maintainer = "MAINTAINER %s" % maintainer
    base_image = "FROM ubuntu:14.04"
    if not dockerfile:
        dockerfile = [
            maintainer,
            "ENV DEBIAN_FRONTEND noninteractive",
            "ENV HOME /root",
            "RUN apt-get update",
            "RUN apt-get install -y --force-yes --no-install-recommends software-properties-common",
        ]

    sub_commands = []
    expose_ports = []
    entry_points = []
    scripts      = []
    env          = []
    workdir      = []
    maintainers  = []
    for lib in data.get('libs', []):
        sub_commands,expose_ports,entry_points,scripts,env,workdir,maintainers = load_dep(lib)
    # Add all the maintainers collected from scripts

    for maintainer in set(maintainers):
        dockerfile = ["MAINTAINER %s" % maintainer]+dockerfile

    dockerfile.extend(sub_commands)
    dockerfile.extend([
        "RUN apt-get purge software-properties-common -y --force-yes",
        "RUN apt-get -y autoclean",
        "RUN apt-get -y autoremove",
        "RUN rm -rf /var/lib/apt/lists/*",
        "RUN rm -rf /tmp/*",
        "RUN rm -rf /var/tmp/*"
    ])
    for _env in env:
        dockerfile.append("ENV %s" % _env)
    # Honour last workdir
    if workdir:
        dockerfile.append("WORKDIR %s" % workdir[-1])

    # Add expose ports to final Dockerfile
    if expose_ports:
        dockerfile.append("EXPOSE %s" % " ".join(expose_ports))

    if entry_points:
        entry_point = entry_points[-1]
        scripts.append(" ".join(entry_point))
    exec_command = 'echo -e "%s" >> /entrypoint.sh' % ("\\n".join(["#!/bin/bash"]+scripts))
    dockerfile.append("RUN bash -c '%s'" % exec_command)
    dockerfile.append("RUN chmod +x /entrypoint.sh")
    dockerfile.append("ENTRYPOINT %s" % json.dumps(["/entrypoint.sh"]))
    
    dockerfile = "\n".join([base_image]+dockerfile)
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
