from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint
year=2023
day=5
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.split("\n\n")

Seeds = [int(i) for i in input[0].split(" ")[1:]]
maps = [input[i].split("\n")[1:] for i in range(1, len(input))]
maps = [[[int(i) for i in line.split()] for line in map] for map in maps]
solutions=[]
for val in Seeds:
    for map in maps:
        for line in map:
            if val>=line[1] and val-line[1]<line[2]:
                val=line[0]+val-line[1]
                break
    solutions.append(val)

submit(min(solutions), part=1, year=year, day=day)

val_ranges = Seeds
for map in maps:
    new_val_ranges = []
    while len(val_ranges)>0:
        changed=False
        for line in map:
            x, x_range=val_ranges[0:2]
            if max(line[1],x)<min(x+x_range, line[1]+line[2]):
                # Found an overlap, get new ranges in new and old list
                val_ranges.pop(0)
                val_ranges.pop(0)
                if x<line[1]:
                    val_ranges.append(x)
                    val_ranges.append(line[1]-x)
                if x+x_range>line[1]+line[2]:
                    val_ranges.append(line[1]+line[2])
                    val_ranges.append(x+x_range-line[1]-line[2])
                new_val_ranges.append(line[0]-line[1]+max(line[1],x))
                new_val_ranges.append(min(x+x_range, line[1]+line[2])-max(line[1],x))
                changed=True
                break
        if not changed:
            # No overlaps found, append old range to new list
            new_val_ranges.append(val_ranges.pop(0))
            new_val_ranges.append(val_ranges.pop(0))
    val_ranges=new_val_ranges

submit(min([val_ranges[i] for i in range(0,len(val_ranges),2)]), part=2, year=year, day=day)