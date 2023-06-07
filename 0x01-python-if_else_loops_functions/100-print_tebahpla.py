#!/usr/bin/python3
for i in range(122, 96, -1):
    offset = 0
    if (i % 2):
        offset = -32
    print("{}".format(chr(i + offset)), end='')
