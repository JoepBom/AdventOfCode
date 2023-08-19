f = open("C:/Users/joep_/Documents/AdventOfCode/2020/11/input.txt", "r")
input1=[[]]
for x in f:
    input1.append("L"+x[:-1]+"L")
input1[0]=len(input1[1])*"L"
input1.append(len(input1[1])*"L")

Directions=[[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,-1],[0,1]]
Different=True
countert=0
while Different:
    Different=False
    newinput=[len(input1[1])*"L"]
    for i in range(1,len(input1)-1):
        line='L'
        for j in range(1,len(input1[1])-1):
            AdjecentSeats=[]
            if not input1[i][j]== ".":
                for k in Directions:
                    count=1
                    while input1[i+count*k[0]][j+count*k[1]]=='.':
                        count+=1
                    AdjecentSeats.append(input1[i+count*k[0]][j+count*k[1]])
                if(input1[i][j]=='L'):
                    if any(x=='#' for x in AdjecentSeats):
                        line+='L'
                    else:
                        Different=True
                        line+='#'
                else:
                    if sum(map(lambda x : x == '#', AdjecentSeats))>=5:
                        line+='L'
                        Different=True
                    else:
                        line+='#'
            else:
                line+='.'
        line+='L'
        newinput.append(line)
    newinput.append(len(input1[1])*'L')
    input1=newinput
    countert+=1
counter=0

for i in input1:
    counter+=sum(map(lambda x : x=='#', i))
print(counter)
print(countert)