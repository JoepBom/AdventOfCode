import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/3/input.txt", "r")
input=[]
tot1=0
tot2=0
lines = f.readlines()
count = 0 
group = list()
for line in lines:
    x=line.strip()
    x0 = x[:int(len(x)/2)]
    x1 = x[int(len(x)/2):]
    char = set(x0).intersection(set(x1))
    asciivalue = ord(list(char)[0])
    if asciivalue < 91:
        tot1 += asciivalue - 38
    else:
        tot1 += asciivalue - 96
    group.append(set(x))
    count+=1
    if count == 3:
        badge = list(group[0].intersection(group[1]).intersection(group[2]))[0]
        print(badge)
        asciivalue = ord(badge)
        if asciivalue < 91:
            tot2 += asciivalue - 38
        else:
            tot2 += asciivalue - 96
        group = list()
        count =0

print(tot1)
print(tot2)
    
