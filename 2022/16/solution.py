from pprint import pprint
import numpy as np
import random
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\16\input.txt", "r")
input = dict()
for line in file.readlines():
    i=line.strip().split(" ")
    input[i[1]]=dict()
    input[i[1]]["flow"]=int(i[4][5:-1])
    input[i[1]]["tunnels"]=list()
    for j in range(9,len(i)):
        if j != len(i)-1:
            input[i[1]]["tunnels"].append(i[j][:-1])
        else:
            input[i[1]]["tunnels"].append(i[j])
valve_amount=len(input.keys())
distances = dict()
for i in input.keys():
    count = 2
    distances[i]={i: 0}
    to_visit = input[i]["tunnels"]
    while len(distances[i].keys()) < valve_amount:
        new_to_visit = []
        for j in to_visit:
            distances[i][j]=count
            for k in input[j]["tunnels"]:
                if k not in distances[i].keys() and k not in new_to_visit:
                    new_to_visit.append(k)
        to_visit = new_to_visit
        count+=1

            
to_keep = [i for i in distances.keys() if input[i]["flow"] != 0]
to_remove = set(i for i in distances.keys() if input[i]["flow"] == 0)
to_remove.remove("AA")
valve_amount=len([i for i in distances.keys() if input[i]["flow"] != 0])
for i in to_remove:
    for j in distances.keys():
        del distances[j][i]
    del distances[i]

for i in distances.keys():
    del distances[i][i]
pprint(distances)

potential_flows = dict()
actual_flows = dict()
max_potential_flow = 0
for i in distances["AA"].keys():
    max_potential_flow+=input[i]["flow"]*(30-distances["AA"][i])
potential_flows[("AA",)]=max_potential_flow
actual_flows[("AA",)]=0
print(max_potential_flow)

# for i in distances["AA"].keys():
#     time = 30-distances["AA"][i]-1
#     cur_flow = time*input[i]["flow"]
#     tot_potential_flow = cur_flow
#     actual_flows[("AA",i)]=cur_flow
#     for j in distances[i].keys():
#         if j != "AA":
#             potential_time=time-distances[i][j]-1
#             tot_potential_flow+=potential_time*input[j]["flow"]
#     potential_flows[("AA",i)]=tot_potential_flow

# pprint(potential_flows)
# pprint(actual_flows)

def calc_flows(cur_path, cur_flow, distances, potential_flows, actual_flows, time):
    # Calculate time of path
    for i in range(len(cur_path)-1):
        time-=distances[cur_path[i]][cur_path[i+1]]
    for i in distances[cur_path[-1]].keys():
        if i not in cur_path:
            path=cur_path.copy()
            path.append(i)
            new_time=time
            new_time-=distances[cur_path[-1]][i]
            if time<=0:
                continue
            actual_flows[tuple(path)]=cur_flow+new_time*input[i]["flow"]
            potential_flows[tuple(path)]=cur_flow+new_time*input[i]["flow"]
            for j in distances[i].keys():
                if j not in path:
                    potential_flows[tuple(path)]+=(new_time-distances[i][j])*input[j]["flow"]
    return

while len(potential_flows)>0:
    max_potential_flow = 0
    max_potential_flow_path = None
    for i in potential_flows.keys():
        if potential_flows[i]>max_potential_flow:
            max_potential_flow = potential_flows[i]
            max_potential_flow_path = i
    calc_flows(list(max_potential_flow_path), actual_flows[max_potential_flow_path], distances, potential_flows, actual_flows, 30)
    del potential_flows[max_potential_flow_path]
    max_actual_flow = max(actual_flows.values())
    to_delete = []
    for i in potential_flows.keys():
        if potential_flows[i]<=max_actual_flow:
            to_delete.append(i)
    for i in to_delete:
        del potential_flows[i]

# pprint(actual_flows)
print([(i, j) for (i,j) in actual_flows.items() if j == max(actual_flows.values())])

# part 2
# sample half the valves
max_actual_flows = dict()
count=0
valves = [i for i in distances.keys() if i != "AA"]
#create list of all possible combinations of 8 valves
combins = list(combinations(valves, 1)) + list(combinations(valves, 2)) + list(combinations(valves, 3)) + list(combinations(valves, 4)) + list(combinations(valves, 5)) + list(combinations(valves, 6))+ list(combinations(valves, 7))

print(len(combins))
for i in combins:
    first_half=list(i)
    second_half = [i for i in distances.keys() if i not in first_half]
    first_half.append("AA")
    second_half.append("AA")
    distances_1 = dict()
    distances_2 = dict()
    for i in first_half:
        distances_1[i]=dict()
        for j in first_half:
            if j != i:
                distances_1[i][j]=distances[i][j]
    for i in second_half:
        distances_2[i]=dict()
        for j in second_half:
            if j != i:
                distances_2[i][j]=distances[i][j]
        
    potential_flows_1 = dict()
    actual_flows_1 = dict()
    max_potential_flow_1 = 0
    for i in distances_1["AA"].keys():
        max_potential_flow_1+=input[i]["flow"]*(26-distances_1["AA"][i])
    potential_flows_1[("AA",)]=max_potential_flow_1
    actual_flows_1[("AA",)]=0
    while len(potential_flows_1)>0:
        max_potential_flow_1 = 0
        max_potential_flow_path_1 = None
        for i in potential_flows_1.keys():
            if potential_flows_1[i]>max_potential_flow_1:
                max_potential_flow_1 = potential_flows_1[i]
                max_potential_flow_path_1 = i
        if max_potential_flow_path_1 is not None:
            calc_flows(list(max_potential_flow_path_1), actual_flows_1[max_potential_flow_path_1], distances_1, potential_flows_1, actual_flows_1, 26)
            del potential_flows_1[max_potential_flow_path_1]
        max_actual_flow_1 = max(actual_flows_1.values())
        to_delete = []
        for i in potential_flows_1.keys():
            if potential_flows_1[i]<=max_actual_flow_1:
                to_delete.append(i)
        for i in to_delete:
            del potential_flows_1[i]

    potential_flows_2 = dict()
    actual_flows_2 = dict()
    max_potential_flow_2 = 0
    for i in distances_2["AA"].keys():
        max_potential_flow_2+=input[i]["flow"]*(26-distances_2["AA"][i])
    potential_flows_2[("AA",)]=max_potential_flow_2
    actual_flows_2[("AA",)]=0
    while len(potential_flows_2)>0:
        max_potential_flow_2 = 0
        max_potential_flow_path_2 = None
        for i in potential_flows_2.keys():
            if potential_flows_2[i]>max_potential_flow_2:
                max_potential_flow_2 = potential_flows_2[i]
                max_potential_flow_path_2 = i
        if max_potential_flow_path_2 is not None:
            calc_flows(list(max_potential_flow_path_2), actual_flows_2[max_potential_flow_path_2], distances_2, potential_flows_2, actual_flows_2, 26)
            del potential_flows_2[max_potential_flow_path_2]
        max_actual_flow_2 = max(actual_flows_2.values())
        to_delete = []
        for i in potential_flows_2.keys():
            if potential_flows_2[i]<=max_actual_flow_2:
                to_delete.append(i)
        for i in to_delete:
            del potential_flows_2[i]
    count+=1 
    path1=[i for i in actual_flows_1.keys() if actual_flows_1[i] == max(actual_flows_1.values())][0]
    path2=[i for i in actual_flows_2.keys() if actual_flows_2[i] == max(actual_flows_2.values())][0]
    max_actual_flows[(path1, path2)]=max_actual_flow_1+max_actual_flow_2
    if count%100==0:
        print("amount of options checked: ", count, "/", len(combins))
        print(np.max(list(max_actual_flows.values())))

print([(i,j) for (i,j) in max_actual_flows.items() if j == np.max(list(max_actual_flows.values()))])














quit()
#part 2 first try

potential_flows = dict()
actual_flows = dict()
max_potential_flow = 0
for i in distances["AA"].keys():
    max_potential_flow+=input[i]["flow"]*(26-distances["AA"][i])
potential_flows[(("AA",),("AA",))]=max_potential_flow
actual_flows[(("AA",),("AA",))]=0
print(max_potential_flow)

for i in distances["AA"].keys():
    time = 26-distances["AA"][i]
    cur_flow = time*input[i]["flow"]
    tot_potential_flow = cur_flow
    actual_flows[("AA",i), ("AA",)]=cur_flow
    for j in distances[i].keys():
        if j != "AA":
            potential_time=time-distances[i][j]
            tot_potential_flow+=potential_time*input[j]["flow"]
    potential_flows[("AA",i), ("AA",)]=tot_potential_flow
del potential_flows[(("AA",),("AA",))]
# pprint(potential_flows)
# pprint(actual_flows)

def calc_flows(cur_path, cur_flow):
    # Calculate time of path
    # me
    time = [26,26]
    for k in range(2):
        for i in range(len(cur_path[k])-1):
            time[k]-=distances[cur_path[k][i]][cur_path[k][i+1]]
    for k in range(2):
        list1=[i for i in distances[cur_path[k][-1]].keys()].copy()
        random.shuffle(list1)
        for i in list1:
            if i not in cur_path[0] and i not in cur_path[1]:
                path=[cur_path[0].copy(),cur_path[1].copy()]
                path[k].append(i)
                new_time=time.copy()
                new_time[k]-=distances[cur_path[k][-1]][i]
                if new_time[k]<=0:
                    continue
                actual_flows[(tuple(path[0]),tuple(path[1]))]=cur_flow+new_time[k]*input[i]["flow"]
                potential_flows[(tuple(path[0]),tuple(path[1]))]=cur_flow+new_time[k]*input[i]["flow"]
                for j in distances[i].keys():
                    if j not in path[0] and j not in path[1]:
                        potential_flows[(tuple(path[0]),tuple(path[1]))]+=max((new_time[0]-distances[path[0][-1]][j])*input[j]["flow"], (new_time[1]-distances[path[1][-1]][j])*input[j]["flow"])
    return

count=1
while len(potential_flows)>0:
    if count%100==0:
        print(len(potential_flows), max_actual_flow, np.min(list(potential_flows.values())), np.mean(list(potential_flows.values())), np.max(list(potential_flows.values())), np.std(list(potential_flows.values())))
    max_potential_flow = 0
    visited_valves = 0
    max_potential_flow_path = None
    for i in potential_flows.keys():
        # if visited_valves<=len(i[0])+len(i[1]):
            if potential_flows[i]>max_potential_flow:
                max_potential_flow= potential_flows[i]
                max_potential_flow_path = i
    calc_flows([list(max_potential_flow_path[0]),list(max_potential_flow_path[1])] , actual_flows[max_potential_flow_path])
    del potential_flows[max_potential_flow_path]
    max_actual_flow = max(actual_flows.values())
    to_delete = []
    for i in potential_flows.keys():
        if potential_flows[i]<=max_actual_flow:
            to_delete.append(i)
    for i in to_delete:
        del potential_flows[i]
    count+=1

# pprint(actual_flows)
# pprint(potential_flows)
print(max_actual_flow)
print([(i, j) for (i,j) in actual_flows.items() if j == max_actual_flow])


# part 2 second try


# maximize sum(X[node, t, person]*flow[node]*t for node in nodes for t in range(27) for person in [0,1])
# s.t.
# sum(X[node, t] for node in nodes for t in range(27)) <= 1 (each node is visited at most once)
# Y[node1, node2] = sum(X[node2, t+ dist[node1,node2]] * X[node1, t] for t in range(27-dist[node1,node2]) (node1 is visited just before node2)
# sum(Y[node1, node2] for node2 in nodes) <= 1 (each node is visited just after at most one other node)
# sum(Y[node1, node2] for node1 in nodes except "AA") <= 1 (each node is visited just before at most one other node)
# sum(Y["AA", node2] for node1 in nodes except "ZZ") <= 1 (each node is visited just after at most one other node)
# X[node, t] = 1 if node is visited at time left t, 0 otherwise
# Y[node1, node2] = 1 if node1 is visited just before node2, 0 otherwise


# split in half
# do algorithm for both halves, add





