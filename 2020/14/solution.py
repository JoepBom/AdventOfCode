import re
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/14/input.txt", "r")
input=f.read().splitlines()
input2=[]
for i in input:
    i=i.replace('[',' ').replace(']','').replace(' = ',' ')
    input2.append(i.split())
print(input2)

Mask=36*'X'
Memory={}
for i in input2:
    if i[0]=='mask':
        Mask=i[1]
        #print(Mask)
    else:
        bitstr="{0:b}".format(int(i[2]))
        #print(bitstr)
        bitstr2=list((36-len(bitstr))*"0"+bitstr)
        for j in range(36):
            if not Mask[j]=='X':
                bitstr2[j]=Mask[j]
        #print(bitstr2)
        Memory[i[1]]=bitstr2
sum=0
for i in Memory:
    sum+=int("".join(Memory[i]),2)
    #print(int(i,2))
print(sum)