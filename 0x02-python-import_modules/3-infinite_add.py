#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    argv = sys.argv[1:]
    i = 0
    mysum = 0
    args = len(argv)
    for i in range(args):
        mysum += int(argv[i])
    print(mysum)
