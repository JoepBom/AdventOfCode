
filepath="2019/3/input.txt"

with open(filepath) as file:
    input = [i.split(",") for i in file.readlines()]

visited = dict()
intersections = dict()
wire=0
for i in input:
    wire+=1
    x=0
    y=0
    steps=0
    for j in i:
        direction = j[0]
        distance = int(j[1:])
        for k in range(distance):
            steps+=1
            if direction == "R":
                x+=1
            if direction == "L":
                x-=1
            if direction == "U":
                y+=1
            if direction == "D":
                y-=1
            if (x,y) not in visited:
                if  wire==1:
                    visited[(x,y)] = steps
            elif wire==2 and (x,y) not in intersections:
                    intersections[(x,y)] = steps+visited[(x,y)]

print(min(intersections.values()))

# print(intersections)

# for i in range(min(x for x,y in visited), max(x for x,y in visited)+1):
#     for j in range(min(y for x,y in visited), max(y for x,y in visited)+1):
#         if (i,j) == (0,0):
#             print("O", end="")
#         if (i,j) in intersections:
#             print("X", end="")
#         elif (i,j) in visited:
#             print(".", end="")
#         else:
#             print(" ", end="")
#     print()
