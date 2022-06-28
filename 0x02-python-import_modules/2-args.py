#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_args = len(argv) - 1
    
    if n_args == 0:
        print("{:d} argument.".format(n_args))
    elif n_args == 1:
        print("{:d} argument:".format(n_args))
    else:
        print("{:d} arguments:".format(n_args))

    if n_args >= 1:
        n = 1
        for arg in argv[1:]:
            print("{:d}: {}".format(n, arg))
            n += 1
            
