import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/2/input.txt", "r")
input=[]
tot=0
lines = f.readlines()
for line in lines:
    x=line.strip()
    # print(x)
    if len(x)>=1:
        tot+= int(x)
        # print(tot)
    else:
        input.append(tot)
        tot=0
print(max(input))
print(sum(sorted(input)[-3:]))
