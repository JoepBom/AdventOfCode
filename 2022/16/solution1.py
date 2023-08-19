import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/16/input_small.txt", "r")
# f = open("C:/Users/joep_/Documents/AdventOfCode/2022/16/input.txt", "r")
input = f.read().splitlines()

tunnels = dict()
valves = dict()

for i in input:
  words = i.split(" ")
  if int(words[4][5:-1])>0:
        valves[words[1]]=int(words[4][5:-1])
  tunnels[words[1]]={j[:-1] for j in words[9:-1]}
  tunnels[words[1]].add(words[-1])

pprint(valves)
pprint(tunnels)

distance_table = {key: {key: 0} for key in tunnels.keys()}
step=0
while len(set(key for key in distance_table if len(distance_table[key])!=len(distance_table)))>0:
  for key in distance_table:
    for key1 in set(key1 for key1 in distance_table[key] if distance_table[key][key1]==step):
          for neighbour in tunnels[key1]:
                if neighbour not in distance_table[key]:
                      distance_table[key][neighbour]=step+1
                      distance_table[neighbour][key]=step+1

  step+=1

  minutes_left=30
  potential_routes = {(tuple(),"AA"): (0, 30)} # ({valves_visited}, cur_valve, score, time_left)
  for valve in valves:
    for pot in potential_routes:
      visited_valves = set(list(pot)[0])
      if valve not in visited_valves:
        visited_valves.add(valve)
        potential_routes.add((tuple(visited_valves),valve,))

