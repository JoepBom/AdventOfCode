import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/4/input.txt", "r")
input=[]
for x in f:
    input.append(x)

input2=[]
temp=''
for i in input:
    if(i!='\n'):
        temp+=i[:-1]
        temp+=' '
    else:
        input2.append(temp)
        temp=''
input2.append(temp)

counter=0
for i in input2:
    x=i.split(' ')
    byr=False
    iyr=False
    eyr=False
    hgt=False
    hcl=False
    ecl=False
    pid=False
    cid=False
    for j in x:
        if j[:3]=='byr':
            byr=True
        if j[:3]=='iyr':
            iyr=True
        if j[:3]=='eyr':
            eyr=True
        if j[:3]=='hgt':
            hgt=True
        if j[:3]=='hcl':
            hcl=True
        if j[:3]=='ecl':
            ecl=True
        if j[:3]=='pid':
            pid=True
        if j[:3]=='cid':
            cid=True
    if(byr and iyr and eyr and hgt and hcl and ecl and pid):
        counter+=1
    else:
        print(x)

print(counter)
