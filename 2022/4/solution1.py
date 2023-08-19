import numpy as np
import re

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/4/input.txt", "r")
input=[]
tot1=0
tot2=0
lines = f.readlines()
count = 0
group = list()
for line in lines:  
    x=re.split(",|-",line.strip())
    if (int(x[1])>=int(x[2]) and int(x[0])<=int(x[3])):
        count+=1

print(count)
    
