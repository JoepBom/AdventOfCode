import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/2/input.txt", "r")
input=[]
for x in f:
    y=x.split(" ")
    range=y[0].split("-")
    range[0]=int(range[0])
    range[1]=int(range[1])
    toMatch=y[1][:-1]
    string=y[2][:-1]
    input.append([range,toMatch,string])

counter=0
for tuple in input:
    if (tuple[2][tuple[0][0]-1]==tuple[1]) != (tuple[2][tuple[0][1]-1]==tuple[1]):
        counter+=1

print(counter)

