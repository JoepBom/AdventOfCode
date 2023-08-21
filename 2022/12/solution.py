from pprint import pprint
file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\12\input.txt", "r")

# input = [132*"Z"]
# for i in file.readlines():
#     line = ["Z"]
#     for j in i.strip():
#         line.append(j)
#     line.append("Z")
#     input.append(line)
# line = [132*"Z"]
# input.append(line)

input = [list(i.strip()) for i in file.readlines()]

for x, i in enumerate(input):
    for y, char in enumerate(i):
        if char=="S":
            cur_pos = [x,y]
            input[x][y]="a"
        elif char=="E":
            goal_pos = [x,y]
            input[x][y]="z"

distances = {(goal_pos[0],goal_pos[1]): 0}
visited_nodes = set()
print(cur_pos)
print(goal_pos)
last_node = goal_pos
# while (cur_pos[0],cur_pos[1]) not in distances.keys(): # Activate for part a
while input[last_node[0]][last_node[1]]!="a": # Activate for part b
    # print(distances)
    min_len = min(val for key,val in distances.items() if key not in visited_nodes)
    to_visit = list([(key, val) for key,val in distances.items() if val==min_len and key not in visited_nodes][0])
    x,y=to_visit[0]
    val=to_visit[1]
    for i in [-1,1]:
        try: 
            if ord(input[x][y])-1<=ord(input[x+i][y]):
                if (x+i,y) not in distances.keys():
                    distances[(x+i,y)]=val+1
                else:
                    distances[(x+i,y)] = min(distances[(x+i,y)], val+1 )
        except:
            a=""
        try: 
            if ord(input[x][y])-1<=ord(input[x][y+i]):
                if (x,y+i) not in distances.keys():
                    distances[(x,y+i)]=val+1
                else:
                    distances[(x,y+i)] = min(distances[(x,y+i)], val+1 )
        except:
            a=""
    visited_nodes.add((x,y))
    last_node=[x,y]


print(distances[(last_node[0],last_node[1])])

        
