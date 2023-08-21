from pprint import pprint
file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\14\input.txt", "r")
input = []
for line in file.readlines():
    input.append([[int(i) for i in j.split(",")] for j in line.strip().split(" -> ")])

blocked_points = set()
# last_point = None
for path in input:
    last_point = None
    for cur_point in path:
        if last_point is None:
            last_point = cur_point
            continue
        direction = (1 if cur_point[0]-last_point[0] > 0 or cur_point[1]-last_point[1] > 0 else -1)
        for dx in range(0, cur_point[0]-last_point[0]+direction, direction):
            for dy in range(0, cur_point[1]-last_point[1]+direction, direction):
                # print(dx,dy)
                blocked_points.add((cur_point[0]-dx, cur_point[1]-dy))
        last_point = cur_point
    

rocks = {i for i in blocked_points}
lowest_point = max(y for x,y in blocked_points)
y=0
while y<lowest_point:
    y=0
    x=500
    stopped=False
    while not stopped and y<lowest_point:
        if (x,y+1) not in blocked_points:
            y=y+1
            continue
        if (x-1,y+1) not in blocked_points:
            x=x-1
            y=y+1
            continue
        if (x+1,y+1) not in blocked_points:
            x=x+1
            y=y+1
            continue            
        stopped=True
        blocked_points.add((x,y))

for y in range(min(y for x,y in blocked_points), max(y for x,y in blocked_points)+1 ):
    line = ""
    for x in range(min(x for x,y in blocked_points), max(x for x,y in blocked_points)+1):
        line+=("#" if (x,y) in rocks else ("o" if (x,y) in blocked_points else "."))
    print(line)

print(len(blocked_points)- len(rocks))

blocked_points = {i for i in rocks}
while (500,0) not in blocked_points:
    y=0
    x=500
    stopped=False
    while not stopped:
        # print(x,y)
        if y==lowest_point+1:
            blocked_points.add((x,y))
            stopped=True
            # print(x,y)
            continue
        if (x,y+1) not in blocked_points:
            y=y+1
            continue
        if (x-1,y+1) not in blocked_points:
            x=x-1
            y=y+1
            continue
        if (x+1,y+1) not in blocked_points:
            x=x+1
            y=y+1
            continue            
        stopped=True
        blocked_points.add((x,y))
        # print(x,y)
file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\14\output.txt", "w")
for y in range(min(y for x,y in blocked_points), max(y for x,y in blocked_points)+1 ):
    line = ""
    for x in range(min(x for x,y in blocked_points), max(x for x,y in blocked_points)+1):
        line+=("#" if (x,y) in rocks else ("o" if (x,y) in blocked_points else "."))
    file.write(line+"\n")

print(len(blocked_points)- len(rocks))