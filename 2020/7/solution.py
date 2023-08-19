import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/7/input.txt", "r")
input=[]
for x in f:
    input.append(x[:-2])
input2=[]
amount2=[]

for i in input:
    j=i.split('contain ')
    m=['',[]]
    m[0]=j[0][:-6]
    j[1]=j[1].replace(' bags','').replace(' bag','').split(", ")
    amounts=[]
    for k in j[1]:
        if(k[:2]!='no'):
            l=int(k[:1])
            amounts.append(l)
            m[1].append(k.replace(str(l)+' ',''))
        else:
            amounts.append(0)
            m[1].append(k.replace('no ',''))
    input2.append(m)
    amount2.append(amounts)
input2=np.array(input2)
amount2=np.array(amount2)
print(input2)

def RecursiveFunction(color,origin):
    if color=='shiny gold':
        return True
    index=np.where(input2==color)[0]
    for i in input2[index,1]:
        for j in i:
            if(RecursiveFunction(j, origin)):
                return True
    return False

counter=0
for i in input2[:,0]:
    if(RecursiveFunction(i,i)):
        print(i)
        counter+=1

print(counter-1)
