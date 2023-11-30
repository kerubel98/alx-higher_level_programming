#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1

    sum = 0

    if argc == 0:
        print(sum)
    elif argc == 1:
        print("{:d}".format(int(argv[1])))
    else:
        while argc >= 1:
            sum += int(argv[argc])
            argc -= 1
        print("{:d}".format(sum))
