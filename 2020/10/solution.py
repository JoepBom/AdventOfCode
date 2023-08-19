f = open("C:/Users/joep_/Documents/AdventOfCode/2020/10/input.txt", "r")
input1=[0]
for x in f:
    input1.append(int(x[:-1]))
input1.sort()

def FindForced(meuk):
    forced=[0]
    for i in range(1,len(meuk)):
        if meuk[i]-meuk[i-1] == 3:
            forced.append(meuk[i-1])
            forced.append(meuk[i])
    forced.append(max(meuk))
    forced=list(set(forced))
    forced.sort()
    return forced

def CountCombinations(zooi, forced):
    diff=[i for i in zooi + forced if i not in zooi or i not in forced]
    res=1
    for i in range(1,len(forced)):
        meuk=[j for j in diff if j>forced[i-1] and j<forced[i]]
        comb=2**len(meuk)
        if forced[i]-forced[i-1]==4 and not comb==1:
            comb-=1
        res*=comb
    return res

forced=FindForced(input1)
print(CountCombinations(input1,forced))


