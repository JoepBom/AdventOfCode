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
        self.xLoc=0
        self.yLoc=0
        self.wpX=10
        self.wpY=1

    def turn(self,degr):
        for i in range(int((degr%360)/90)):
            temp=self.wpX
            self.wpX=self.wpY
            self.wpY=-temp
    def move(self,amount):
        self.xLoc+=amount*self.wpX
        self.yLoc+=amount*self.wpY
    def push(self,amount,Dir):
        if Dir=='N':
            self.wpY+=amount
        elif Dir=='S':
            self.wpY-=amount
        elif Dir=='E':
            self.wpX+=amount
        elif Dir=='W':
            self.wpX-=amount
    

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