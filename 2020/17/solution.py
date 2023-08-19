import numpy
from pprint import pprint
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/17/input copy.txt", "r")
input=f.read().splitlines()
n=22
start=7
cubes=numpy.zeros((n-2,n-2,n,n))
countY=start
countZ=start
countW=start
for i in input:
    countX=start
    for k in i:
        if k == '#':
            cubes[countW,countZ,countY,countX]=1
        countX+=1
    countY+=1


for times in range(6):
    #print(cubes[start-(times):n-(start-(times-2)),start-(times):n-(start-(times-2)),start-times:n-(start-times),start-times:n-(start-times)])
    newCubes=cubes.copy()
    for x in range(1,n-3):
        for y in range(1,n-3):
            for z in range(1,n-1):
                for w in range(1,n-1):
                    NeighboursActive=0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                for dw in [-1,0,1]:
                                    if not (dx==0 and dy==0 and dz==0 and dw==0):
                                        NeighboursActive+=cubes[x+dx,y+dy,z+dz,w+dw]
                    if cubes[x,y,z,w]==0:
                        if NeighboursActive==3:
                            newCubes[x,y,z,w]=1
                    else:
                        if not (NeighboursActive==2 or NeighboursActive==3):
                            newCubes[x,y,z,w]=0
    cubes=newCubes
#print(cubes)

print(sum(sum(sum(sum(cubes)))))
