#!/usr/bin/python3
for comb2 in range(100):
    if comb2 != 99:
        print("{}{}, ".format(int(comb2 / 10), comb2%% 10), end="")
    else:
        print("{}{}, ".format(int(comb2 / 10), comb2 % 10))
