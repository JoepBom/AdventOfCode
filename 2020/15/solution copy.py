import re
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/14/input.txt", "r")
input=f.read().splitlines()
input2=[]
for i in input:
    i=re.split(r'\[|]*\s=\s',i)
    input2.append(i)

Mask=36*'0'
Memory={}
for i in input2:
    if i[0]=='mask':
        Mask=i[1]
        #print(Mask)
    else:
        bitstr="{0:b}".format(int(i[1]))
        adrList=[list((36-len(bitstr))*"0"+bitstr)]
        for j in range(36):
            if Mask[j]=='1':
                for a in adrList:
                    a[j]='1'
            elif Mask[j]=='X':
                adrList2=[]
                for a in adrList:
                    a[j]='0'
                    adrList2.append(a.copy())
                    a[j]='1'
                    adrList2.append(a.copy())
                adrList=adrList2
        #print(len(adrList))
        for a in adrList:
            Memory["".join(a)]=i[2]
sum=0
for i in Memory:
    sum+=int(Memory[i])
print(sum)