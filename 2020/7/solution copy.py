import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/7/input.txt", "r")
input=[]
for x in f:
    input.append(x[:-2])
input2=[]

for i in input:
    j=i.split('contain ')
    m=['',[]]
    j[0]=j[0][:-6]
    j[1]=j[1].replace(' bags','').replace(' bag','').split(", ")
    input2.append(j)
input2=np.array(input2)

def RecursiveFunction(color):
    sum=1
    index=np.where(input2==color)[0]
    for i in input2[index,1]:
        for j in i:
            if(j[0]!='n'):
                print(j)
                sum+=int(j[0])*RecursiveFunction(j[2:])
    return sum

print(RecursiveFunction('shiny gold')-1)
