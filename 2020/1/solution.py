import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/1/input.txt", "r")
input=[]
for x in f:
    input.append(int(x))

input=np.array(input)
input.sort()
forwardCount=0
backwardCount=len(input)-1
while forwardCount!=backwardCount:
    if input[forwardCount]+input[backwardCount]<2020:
        forwardCount=forwardCount+1
    elif input[forwardCount]+input[backwardCount]>2020:
        backwardCount=backwardCount-1
    else:
        print(input[forwardCount]," * ",input[backwardCount]," = ",input[forwardCount]*input[backwardCount])
        break