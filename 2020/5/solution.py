import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/5/input.txt", "r")
input=[]
for x in f:
    input.append(int(x[:-1].replace("F",'0').replace('B','1').replace('L','0').replace('R','1'),2))

input.sort()
prev=35
for i in input:
    if prev+1!=i:
        print(prev)
        print(i)
    prev=i