import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/3/input.txt", "r")
input=[]
for x in f:
    input.append(x[:-1])

print(input)
counter1=0
startingPoint=[0,0]
yLength=len(input)
xLength=len(input[0])
for yCoord in range(0,yLength):
    Point=input[yCoord][(1*yCoord) % xLength]
    if Point == "#":
        counter1+=1

counter2=0
startingPoint=[0,0]
for yCoord in range(0,yLength):
    Point=input[yCoord][(3*yCoord) % xLength]
    if Point == "#":
        counter2+=1

counter3=0
startingPoint=[0,0]
for yCoord in range(0,yLength):
    Point=input[yCoord][(5*yCoord) % xLength]
    if Point == "#":
        counter3+=1


counter4=0
startingPoint=[0,0]
for yCoord in range(0,yLength):
    Point=input[yCoord][(7*yCoord) % xLength]
    if Point == "#":
        counter4+=1

counter5=0
startingPoint=[0,0]
for yCoord in range(0,int(yLength/2)+1):
    Point=input[2*yCoord][yCoord % xLength]
    if Point == "#":
        counter5+=1
print(counter1)
print(counter2)
print(counter3)
print(counter4)
print(counter5)
print(counter1*counter2*counter3*counter4*counter5)