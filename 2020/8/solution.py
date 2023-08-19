import numpy as np
import copy
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/8/input.txt", "r")
input=[]
for x in f:
    input.append(x[:-1].split(' '))

input.append('The End!')

inputs=[]

for i in range(0,len(input)-1):
    if(input[i][0]!='acc'):
        input2=copy.deepcopy(input)
        if input2[i][0]=='jmp':
            input2[i][0]='nop'
        else:
            input2[i][0]='jmp'
        acc=0
        visited=(len(input2)+1)*[False]
        curLine=0
        loopFound=False
        while((not visited[curLine]) and (input2[curLine]!='The End!')):
            visited[curLine]=True
            if(input2[curLine][0]=='nop'):
                curLine+=1
            elif(input2[curLine][0]=='acc'):
                if(input2[curLine][1][0]=='+'):
                    acc+=int(input2[curLine][1][1:])
                else:
                    acc-=int(input2[curLine][1][1:])
                curLine+=1
            elif(input2[curLine][0]=='jmp'):
                if(input2[curLine][1][0]=='+'):
                    curLine+=int(input2[curLine][1][1:])
                else:
                    curLine-=int(input2[curLine][1][1:])
            if(curLine==637):
                print('The End!')
            if(visited[curLine]==True):
                loopFound=True
        if not loopFound:
            print('solution found by changing '+str(i))
            print('acc = '+str(acc))
