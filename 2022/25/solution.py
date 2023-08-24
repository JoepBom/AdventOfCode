from pprint import pprint
import numpy as np
import random
import re
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\25\input.txt", "r")
input = file.readlines()
numbers = [line.strip()[::-1] for line in input]
# numbers = ["02", "02"]
pprint(numbers)
mapping_1 = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

mapping_2 = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
}

def add_numbers(nr1, nr2):
    res = ""
    keep = 0
    for i in range(max(len(nr1), len(nr2))):
        number = (
            (mapping_1[nr1[i]] if i < len(nr1) else 0)
             + (mapping_1[nr2[i]] if i < len(nr2) else 0)
             + keep)
        # print("nr: ", number)
        keep = ((number+2) // 5)
        res += mapping_2[((number+2) % 5)-2]
        # print("keep: ",keep)
        # print("res: ",res)
    if keep > 0:
        res += mapping_2[keep]
        # print("res: ",res)
    return res


res=""
for nr in numbers:
    if res == "":
        res = nr
    else:
        res = add_numbers(res, nr)
print(res[::-1])