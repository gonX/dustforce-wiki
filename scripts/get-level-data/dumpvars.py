#!/usr/bin/env python3
#
# usage: ./$0 <map filename>
# change path as desired

from dustmaker import *
import sys
import os

srcpath = "/home/gonx/.steam/steam/steamapps/common/Dustforce/content/levels2/"
pathexists = os.path.isdir(srcpath)

if len(sys.argv) <= 1:
    print("Usage: {} <map filename>\n".format(sys.argv[0]))
    print("Configured map path: {}\n            (exists: {})".format(srcpath, pathexists))
    sys.exit(1)

if not pathexists:
    print("The configured map path '{}' does not exist.".format(srcpath))
    sys.exit(1)

with open(os.path.join(srcpath, sys.argv[1]), "rb") as f:
    map = read_map(f.read())
    for (x, y) in map.vars.items():
        print("{}: {}".format(x, y.value))
