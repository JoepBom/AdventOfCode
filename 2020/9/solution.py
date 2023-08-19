f = open("C:/Users/joep_/Documents/AdventOfCode/2020/9/input.txt", "r")
input=[]
for x in f:
    input.append(int(x[:-1]))

input.append('The End!')

#sRunningSums=24^2*[0]
#first 25 are i-25 + all in range(i-24,i-1), next 25 are i-24


for i in range(25,len(input)):
    Good=False
    for j in range(1,26):
        ji=input[i-j]
        for k in range(j+1,26):   
            ki=input[i-k]
            if(ji+ki==input[i]):
                Good=True
                break
        if Good:
            break
    if not Good:
        print(i)
        print(input[i])
        break