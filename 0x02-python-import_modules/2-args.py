#!/usr/bin/python3
import sys

argv = sys.argv
plur = "s"
dot = ":"
i = 1
args = len(argv) - 1
if args == 1:
    plur = ""
if args == 0:
    dot = "."
print("{} argument{}{}".format(str(args), plur, dot))
if args:
    while not(i == args + 1):
        print("{}: {}".format(str(i), argv[i]))
        i += 1
