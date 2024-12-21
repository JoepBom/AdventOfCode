from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
from math import gcd

year=2024
day=8
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()

sat_locs = dict()
for x,y,freq in ((x,y,freq) for x,line in enumerate(input) for y,freq in enumerate(line)):
    if freq == ".":
        continue
    if freq not in sat_locs.keys():
        sat_locs[freq] = {(x,y)} 
    else: 
        sat_locs[freq].add((x,y))

antinodes1 = set()
antinodes2 = set()
for freq, sats in sat_locs.items():
    for sat1, sat2 in combinations(sats, 2):
        diff_vector = ((sat2[0]-sat1[0]),(sat2[1]-sat1[1]))
        gcd_vec = gcd(diff_vector[0], diff_vector[1])
        min_vector = (diff_vector[0]/gcd_vec, diff_vector[1]/gcd_vec)
        x,y = sat1
        antinodes1.add((x+2*(sat2[0]-sat1[0]), y+2*(sat2[1]-sat1[1])))
        while 0<=x<len(input) and 0<=y<len(input[0]):
            antinodes2.add((x,y))
            x+=min_vector[0]
            y+=min_vector[1]
        x,y = sat2
        antinodes1.add((x+2*(sat1[0]-sat2[0]), y+2*(sat1[1]-sat2[1])))
        while 0<=x<len(input) and 0<=y<len(input[0]):
            antinodes2.add((x,y))
            x-=min_vector[0]
            y-=min_vector[1]



            

submit(len([(x,y) for (x,y) in antinodes1 if 0<=x<len(input) and 0<=y<len(input[0])]), part="a", day=day, year=year)
submit(len(antinodes2), part="b", day=day, year=year)