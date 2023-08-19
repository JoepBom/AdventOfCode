import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/5/input.txt", "r")
input=[]
lines = f.readlines()
count = 0
initial_setup = [[],[],[],[],[],[],[],[],[]]
for line in lines:  
    if count<=7:
        for i in range(9):
            if line[4*i+1] != " ":
                initial_setup[i].append(line[4*i+1])
    elif count>8:
        if len(line)>3:
            line = line.strip()
            x = line.split(" ")
            input.append([int(x[1]), int(x[3])-1, int(x[5])-1])
    count+=1
for i in initial_setup:
    i.reverse()

setup = initial_setup

for i in input:
    tempstack = []
    for j in range(i[0]):
        tempstack.append(setup[i[1]].pop())
    for j in range(i[0]):
        setup[i[2]].append(tempstack.pop())

sol = [setup[i].pop() for i in range(len(setup))]
sol2 = ""
for i in sol:
    sol2+=i
print(sol2)


    
