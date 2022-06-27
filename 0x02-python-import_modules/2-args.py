 #!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = 1
    n_args = len(argv) - 1
    
    if n_args == 0:
        print("{:d} argument.".format(n_args))
    elif n_args == 1:
        print("{:d} argument:".format(n_args))
    else:
        print("{:d} arguments:".format(n_args))

    if n_args >= 1:
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
            
