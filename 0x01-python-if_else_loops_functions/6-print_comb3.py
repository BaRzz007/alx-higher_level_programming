#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i == 0 and j == 1:
            print("{}{}".format(i, j), end="")
        elif i > j or i == j:
            continue
        else:
            print(", {}{}".format(i, j), end="")
print()
