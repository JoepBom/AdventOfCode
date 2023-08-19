f = open("C:/Users/joep_/Documents/AdventOfCode/2020/12/input.txt", "r")
input1=[]
for x in f:
    input1.append([x[0],int(x[1:-1])])

class Ship():
    """
    Ship Class
    Dir=0 -> North
    """
    def __init__(self):
        self.Dir=90
        self.xLoc=0
        self.yLoc=0

    def turn(self,degr):
        self.Dir=(self.Dir+degr)%360
    def move(self,amount):
        if self.Dir==0:
            self.yLoc+=amount
        elif self.Dir==180:
            self.yLoc-=amount
        elif self.Dir==90:
            self.xLoc+=amount
        elif self.Dir==270:
            self.xLoc-=amount
    def push(self,amount,Dir):
        if Dir=='N':
            self.yLoc+=amount
        elif Dir=='S':
            self.yLoc-=amount
        elif Dir=='E':
            self.xLoc+=amount
        elif Dir=='W':
            self.xLoc-=amount
    

ship=Ship()
for i in input1:
    if i[0]=='L':
        ship.turn(-i[1])
    elif i[0]=='R':
        ship.turn(i[1])
    elif i[0]=='F':
        ship.move(i[1])
    else:
        ship.push(i[1],i[0])

print(ship.xLoc)
print(ship.yLoc)
print(abs(ship.xLoc)+abs(ship.yLoc))