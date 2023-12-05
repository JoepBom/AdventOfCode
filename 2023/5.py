from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint
year=2023
day=5
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.split("\n\n")

seeds = [int(i) for i in input[0].split(" ")[1:]]
maps = [input[i].split("\n")[1:] for i in range(1, len(input))]
maps = [[tuple(int(i) for i in line.split()) for line in map] for map in maps]
solutions=[]

for value in seeds:
    for map in maps:
        for (dst, src, rng) in map:
            if value>=src and value-src<rng:
                value=dst+value-src
                break
    solutions.append(value)

submit(min(solutions), part=1, year=year, day=day)

value_ranges = seeds
for map in maps:
    new_value_ranges = []
    while len(value_ranges)>0:
        # Until there are no more ranges to map
        # Map ranges to new ranges        
        changed=False
        for (dst, src, rng) in map:
            x, x_range=value_ranges[0:2]
            if max(src,x)<min(x+x_range, src+rng):
                # Found an overlap between the range and the map
                value_ranges.pop(0)
                value_ranges.pop(0)
                if x<src:
                    # If the range starts before the map, the first part of the range still needs to be mapped
                    value_ranges.append(x)
                    value_ranges.append(src-x)
                if x+x_range>src+rng:
                    # If the range ends after the map, the last part of the range still needs to be mapped
                    value_ranges.append(src+rng)
                    value_ranges.append(x+x_range-src-rng)
                # The part of the range that overlaps with the map is mapped to the new range
                new_value_ranges.append(dst-src+max(src,x))
                new_value_ranges.append(min(x+x_range, src+rng)-max(src,x))
                changed=True
                break
        if not changed:
            # No overlaps found between the range and the map, so we keep the range as is
            new_value_ranges.append(value_ranges.pop(0))
            new_value_ranges.append(value_ranges.pop(0))
    value_ranges=new_value_ranges

submit(min([value_ranges[i] for i in range(0,len(value_ranges),2)]), part=2, year=year, day=day)