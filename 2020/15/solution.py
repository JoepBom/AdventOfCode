import re
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/15/input.txt", "r")
input=f.read().splitlines()[0].split(',')
print(input)
dict={}
count=-1
lastNr=input.pop(0)
onebutlast=''
for i in input:
    dict[lastNr]=count
    count+=1
    lastNr=i
while count<29999999:
    if lastNr in dict.keys():
        new=count-dict[lastNr]
        dict[lastNr]=count
        onebutlast=lastNr
        lastNr=str(new)
    else:
        dict[lastNr]=count
        onebutlast=lastNr
        lastNr='0'
    count+=1
print(onebutlast)
print(max([str(key) for key in dict.keys()]))