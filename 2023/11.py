import os
from aocd.models import Puzzle
from aocd import submit

os.environ['AOC_SESSION'] = '53616c7465645f5f5274298a1513bd33b311098204a4e371d2880a4590e8a95748ea42877f6b28b349045dcc1fee6d10f00932890ec53d2fdfe8a068bae08242'

year=2023
day=11

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()


galaxies = [(x,y) for x in range(len(input[0])) for y in range(len(input)) if input[y][x]=="#"]
empty_x = {x for x in range(len(input[0])) if all([input[y][x]=="." for y in range(len(input))])}
empty_y = {y for y in range(len(input)) if all([input[y][x]=="." for x in range(len(input[0]))])}

def get_score(galaxies, expansion_multiplier):
    res = 0
    for i, from_galaxy in enumerate(galaxies):
        for to_galaxy in galaxies[i+1:]:
            res+=abs(to_galaxy[0]-from_galaxy[0]) + abs(to_galaxy[1]-from_galaxy[1])
            for x in empty_x:
                if x>from_galaxy[0] and x<to_galaxy[0] or x<from_galaxy[0] and x>to_galaxy[0]:
                    res+=expansion_multiplier-1
            for y in empty_y:
                if y>from_galaxy[1] and y<to_galaxy[1] or y<from_galaxy[1] and y>to_galaxy[1]:
                    res+=expansion_multiplier-1
    return res

submit(get_score(galaxies, 2), part="a", year=year, day=day)
submit(get_score(galaxies, 1000000), part="b", year=year, day=day)