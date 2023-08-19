import numpy as np
import re

f = open("C:/Users/joep_/Documents/AdventOfCode/2020/4/input.txt", "r")
input=[]
for x in f:
    input.append(x)
print(len(input))
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
            if(int(j[4:])<=2002) and (int(j[4:])>=1920):
                byr=True
        if j[:3]=='iyr':
            if(int(j[4:])<=2020) and (int(j[4:])>=2010):                
                iyr=True
        if j[:3]=='eyr':
            if(int(j[4:])>=2020) and (int(j[4:])<=2030):
                eyr=True
        if j[:3]=='hgt':
            if(j[-2:]=='cm'):
                if(int(j[4:-2])>=150) and (int(j[4:-2])<=193):
                    hgt=True
            if(j[-2:]=='in'):
                if(int(j[4:-2])>=59) and (int(j[4:-2])<=76):        
                    hgt=True
        if j[:3]=='hcl':
            if re.search("^#[0-9a-f]{6}$",j[4:]): 
                hcl=True
        if j[:3]=='ecl':
            if j[4:] in ['amb','blu','brn','gry','grn','hzl','oth']:
                ecl=True
        if j[:3]=='pid':
            if (len(j[4:])==9):
                print(j)
                pid=True
        if j[:3]=='cid':
            cid=True
    if(byr and iyr and eyr and hgt and hcl and ecl and pid):
        counter+=1
    else:
        print(x)

print(counter)
