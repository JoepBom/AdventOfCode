import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/13/input", "r")
input = f.read().splitlines()



def evaluate_line(line):
    res = []
    Nr = ""
    i=0
    while i<len(line):
        if line[i] == "[":
            res1, j = evaluate_line(line[i+1:])
            i+=j+2
            res.append(res1)
        if line[i] in {"0", "1", "2", "3", "4", "5", "6", "7", "8","9"}:
            Nr+=line[i]
        if line[i] == "," and len(Nr)>0:
            res.append(int(Nr))
            Nr = ""
        if line[i] == "]":
            if len(Nr)>0:
                res.append(int(Nr))
            return res, i
        i+=1

lists = []
for line in input:
    if len(line)<2:
        continue
    lists.append(evaluate_line(list(line)[1:])[0])

def compare_lists(list1, list2):
    if type(list1)==int and type(list2)==int:
        if list1<list2:
            return True
        if list1>list2:
            return False
        if list1==list2:
            return None
    if type(list1)==int:
        list1=[list1]
    if type(list2)==int:
        list2=[list2]
    res = None
    for i in range(len(list1)):
        try: 
            res = compare_lists(list1[i], list2[i])
        except:
            return False
        if res is True:
            return True
        if res is False:
            return False
    if len(list2)>len(list1):
        return True
    return res

#part1

res=0
for i in range(0,int(len(lists)/2)):
    # print(lists[2*i], lists[2*i+1])
    if compare_lists(lists[2*i], lists[2*i+1]):
        # print(True)
        res+=i+1

print(res)

#part2

final_lists=[[[2]], [[6]]]

pprint(lists)
for j, list1 in enumerate(lists):
    print(f"inserting {j}/{len(lists)}")
    added=False
    for i, list2 in enumerate(final_lists):
        if compare_lists(list1,list2):
            final_lists.insert(i,list1)
            added=True
            break
    if not added:
        final_lists.append(list1)

sol1=0
sol2=0
for i, res in enumerate(final_lists, 1):
    if len(res)==1 and len(res[0])==1 and res[0][0]==2:
        sol1=i
        print(i)
    if len(res)==1 and len(res[0])==1 and res[0][0]==6:
        sol2=i
        print(i)
print(sol1*sol2)