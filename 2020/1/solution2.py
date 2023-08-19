import numpy as np
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/1/input.txt", "r")
input=[]
for x in f:
    input.append(int(x))

input=np.array(input)
input.sort()
for i in range(0,len(input)):
    nr1=input[i]    
    forwardCount=0
    backwardCount=len(input)-1
    while forwardCount!=backwardCount:
        if i==forwardCount:
            forwardCount+=1
        if i==backwardCount:
            backwardCount=backwardCount-1
        if input[forwardCount]+input[backwardCount]<2020-input[i]:
            forwardCount=forwardCount+1
        elif input[forwardCount]+input[backwardCount]>2020-input[i]:
            backwardCount=backwardCount-1
        else:
            print(input[i], " * ",input[forwardCount]," * ",input[backwardCount]," = ",input[i]*input[forwardCount]*input[backwardCount])
            break