import numpy as np
import re
from pprint import pprint

character_amount = 14
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/6/input.txt", "r")
lines = f.readlines()
for line in lines:  
    input = line.strip()
    break

for i in range(len(input)):
    slice = input[i:i+character_amount]
    if len(set(list(slice)))==character_amount:
        break

print(i+character_amount, slice)



    
