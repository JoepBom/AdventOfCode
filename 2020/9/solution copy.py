f = open("C:/Users/joep_/Documents/AdventOfCode/2020/9/input.txt", "r")
input=[]
for x in f:
    input.append(int(x[:-1]))

meuk=[input[0]]

i=520
k=1
while sum(meuk)!=input[i]:
    if(sum(meuk)>input[i]):
        meuk.pop(0)
    else:
        meuk.append(input[k])
        k+=1
    if(sum(meuk)==input[i]):
        print(min(meuk)+max(meuk))
