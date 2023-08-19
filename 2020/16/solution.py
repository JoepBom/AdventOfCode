import re
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/16/input.txt", "r")
input=f.read().splitlines()
classes=[]
minRanges=[]
maxRanges=[]
while True:
    if input[0]=='':
        input.pop(0)
        break
    classes.append(re.split(r':\s|-|\sor\s',input.pop(0)))
    minRanges.append(int(classes[-1][1]))
    minRanges.append(int(classes[-1][3]))
    maxRanges.append(int(classes[-1][2])+1)
    maxRanges.append(int(classes[-1][4])+1)
yourTicket=[]
while True:
    if input[0]=='':
        input.pop(0)
        break
    yourTicket.append(input.pop(0).split(','))
yourTicket.pop(0)
nearbyTickets=[]
while True:
    if len(input)==0 or input[0]=='':
        if not len(input)==0:
            input.pop(0)
        break
    nearbyTickets.append(input.pop(0).split(','))
nearbyTickets.pop(0)
toRemove=[]
sum=0
for i in nearbyTickets:
    for j in i:
        if not any(int(j) in range(minRanges[a],maxRanges[a]) for a in range(len(minRanges))):
            sum+=int(j)
            toRemove.append(i)
print("Sum of faulty values:",sum)
for i in toRemove:
    nearbyTickets.remove(i)
linking=len(classes)*[-1]
possibleClasses=[]
for j in range(len(nearbyTickets[0])):
    TicketSet=[]
    for i in nearbyTickets:
        temp=set()
        for a in range(len(minRanges)):
            if int(i[j])>=minRanges[a] and int(i[j])<maxRanges[a]:
                temp.add(a//2)
        TicketSet.append(temp)
    possibleClasses.append(set.intersection(*TicketSet))
FinalList=len(classes)*[-1]
Going=True
while Going:
    Going=False
    for i in range(len(possibleClasses)):
        if not len(possibleClasses[i])==0:
            Going=True
            if len(possibleClasses[i])==1:
                Nr=possibleClasses[i].pop()
                FinalList[i]=Nr
                for j in possibleClasses:
                    j.discard(Nr)
prod=1
for i,j in enumerate(yourTicket[0]):
    if classes[FinalList[i]][0][:9]=='departure':
        print(FinalList[i], classes[FinalList[i]][0], j)
        prod=prod*int(j)

print(prod)
    