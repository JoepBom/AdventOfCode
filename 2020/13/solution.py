f = open("C:/Users/joep_/Documents/AdventOfCode/2020/13/input.txt", "r")
input=f.read().splitlines()
goal=int(input[0])
busses=input[1].split(',')

best=100000
bus=''
for i in busses:
    if i!='x':
        if int(i)-(goal%int(i))<=best:
            best=int(i)-(goal%int(i))
            bus=int(i)
print(goal)
print(bus)
print(best)
print(bus*best)