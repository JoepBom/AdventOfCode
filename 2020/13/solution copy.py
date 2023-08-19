f = open("C:/Users/joep_/Documents/AdventOfCode/2020/13/input.txt", "r")
input=f.read().splitlines()
goal=int(input[0])
bus=input[1].split(',')

def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1       
    gcd,x1,y1 = gcdExtended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
    return gcd,x,y 

x=0
mod=[]
a=[]
for i in range(0,len(bus)):
    if not bus[i]=='x':
        mod.append(int(bus[i]))
        a.append((int(bus[i])-i)%int(bus[i]))
while len(a)>1:
    mod1=mod.pop(0)
    mod2=mod.pop(0)
    a1=a.pop(0)%mod1
    a2=a.pop(0)%mod2
    gcd,m1,m2=gcdExtended(mod1,mod2)
    a.append(a1*m2*mod2+a2*m1*mod1)
    mod.append(mod1*mod2)

print(a[0]%mod[0])