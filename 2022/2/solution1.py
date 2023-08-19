import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/2/input.txt", "r")
input=[]
tot1=0
tot2=0
lines = f.readlines()
for line in lines:
    x=line.strip().split()
    print(x)
    x0 = (1 if x[0] == "A" else (0 if x[0] == "B" else 2))
    x1 = (0 if x[1] == "X" else (1 if x[1] == "Y" else 2))
    tot1 += ((x0 + x1) % 3) * 3 + x1 + 1
    tot2 += x1* 3 + ((x1 - x0) % 3) + 1

print(tot1)
print(tot2)