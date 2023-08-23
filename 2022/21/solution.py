import numpy as np
import re
from pprint import pprint
import math

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/21/input", "r")
input = f.read().splitlines()
Monkeys = dict()

for line in input:
    i=line.split()
    if i[0][:-1]=="humn":
        Monkeys[i[0][:-1]]=complex(0,1)
        continue
    if i[0][:-1]=="root":
        Monkeys[i[0][:-1]]=(i[1],"-",i[3])
        continue
    if len(i)>2:
        Monkeys[i[0][:-1]]=(i[1],i[2],i[3])
    else:
        Monkeys[i[0][:-1]]=complex(int(i[1]),0)
    
pprint(Monkeys)
def explore_monkey(name):
    # print(Monkeys[name])
    if type(Monkeys[name])==complex:
        return Monkeys[name]
    res1 = explore_monkey(Monkeys[name][0])
    res2 = explore_monkey(Monkeys[name][2])
    if Monkeys[name][1]=="*":
        if res2.imag == 0:
            print(res1, "*", res2,"=", complex(res1.real * res2.real, res1.imag * res2.real))
            return complex(res1.real * res2.real, res1.imag * res2.real)
        else:
            print(res1, "*", res2,"=", complex(res1.real * res2.real,res1.real * res2.imag))
            return complex(res1.real * res2.real, res1.real * res2.imag)
    if Monkeys[name][1]=="+":
        print(res1, "+", res2, "=", res1 + res2)
        return res1 + res2
    if Monkeys[name][1]=="-":
        print(res1, "-", res2, "=", res1 - res2)
        return res1 - res2
    if Monkeys[name][1]=="/":
        if res2.imag == 0:
            print(res1, "/", res2,"=", complex(res1.real / res2.real,res1.imag / res2.real))
            return complex(res1.real / res2.real, res1.imag/res2.real)
        else:
            print(res1, "/", res2,"=", complex(res1.real / res2.real,res1.real / res2.imag))
            return complex(res1.real / res2.real, res1.real / res2.imag)

    
res=explore_monkey("root")

print(res.real)
print(res.imag)
print(-res.real/res.imag)

