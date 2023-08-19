import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/6/input.txt", "r")
input=[]
for x in f:
    input.append(x[:-1])

input2=[]

def strIntersection(s1, s2):
    out = ""
    for c in s1:
        if c in s2 and not c in out:
            out += c
    return out

temp=False
for i in input:
    if i!='':
        if temp==False:
            temp=i
        else:
            temp=strIntersection(temp, i)
    else:
        input2.append(temp)
        temp=False
input2.append(temp)

print(input2)

count=0
for i in input2:
    if i!= '':
        count+=len(i)

print(count)