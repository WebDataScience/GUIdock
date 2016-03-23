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
    "repo_update": ["RUN apt-get -y update --allow-unauthenticated", None],
    "repo_add"   : ["RUN add-apt-repository -y", lambda command,arg,dep: (command,"'%s'" % arg)],
    "install"    : ["RUN apt-get install -y --force-yes --no-install-recommends", None],
    "purge"      : ["RUN apt-get purge -y --force-yes", None],
    "add"        : ["add", process_add],
    "copy"       : ["copy", process_add]
}

def load_dep(dep, commands=[], expose_ports=[], entry_points=[], scripts=[], env=[], workdir=[], contributors=[], maintainers=[],
                 add_repos=[], install_packages=[], purge_packages=[]):
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
        load_dep(_dep, commands, scripts=scripts, env=env, install_packages=install_packages, purge_packages=purge_packages, 
                     add_repos=add_repos, entry_points=entry_points)
    for command in json_data['commands']:
        try:
            command,arg = command
        except ValueError:
            arg = ""
        if command == "install":
            install_packages.extend(arg.split())
        elif command == "purge":
            purge_packages.extend(arg.split())
        else:
            # Save for matching special commands that are not to be added global list
            orig_command = command
            command,fnc = command_dict.get(command, ["RUN %s" % command, None])
            try:
                command,arg = fnc(command,arg,dep)
            except TypeError:
                pass
            command = "%s %s" % (command, arg)
            if orig_command == "repo_add":
                add_repos.append(command)
            else:
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
        scripts.append("/bin/bash %s \$@" % command_str)
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
            "RUN apt-get install -y --force-yes --no-install-recommends software-properties-common apt-transport-https",
        ]

    # Collect local variables from all components and create a central list of commands
    sub_commands = []
    expose_ports = []
    entry_points = []
    scripts      = []
    env          = []
    workdir      = []
    maintainers  = []
    add_repos    = []
    install_packages = []
    purge_packages   = []
    for lib in data.get('libs', []):
        load_dep(lib, expose_ports=expose_ports, entry_points=entry_points, scripts=scripts, env=env, workdir=workdir,
                     maintainers=maintainers, add_repos=add_repos, commands=sub_commands,
                     install_packages=install_packages, purge_packages=purge_packages)

    # aggregate repo additions
    dockerfile.extend(add_repos)
    dockerfile.append(command_dict['repo_update'][0])

    # aggregate install commands
    command,fnc = command_dict['install']
    dockerfile.append("%s %s" % (command," ".join(install_packages)))

    for maintainer in set(maintainers):
        dockerfile = ["MAINTAINER %s" % maintainer]+dockerfile

    dockerfile.extend(sub_commands)

    # aggregate purge commands
    command,fnc = command_dict['purge']
    dockerfile.append("%s %s" % (command," ".join(purge_packages)))

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
        entry_point = "%s %s" % (" ".join(entry_points[-1]), "\$@")
        scripts.append(entry_point)
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
