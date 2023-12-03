from aocd.models import Puzzle
from aocd import submit
from pprint import pprint
import itertools
import os
import math

year=2023
day=3
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()

symbols = dict()
numbers = dict()
for x, line in enumerate(input):
    number=""
    number_start = (x,0)
    for y, symbol in enumerate(line):
        if not symbol.isdigit():
            if symbol != ".":
                symbols[(x,y)]= symbol
            if len(number)>0:
                numbers[number_start]=number
            number_start = (x,y+1)
            number=""
        if symbol.isdigit():
            number+=symbol
    if len(number)>0:
        numbers[number_start]=number

part1=0
for starting_index, number in numbers.items():
    for (x,y) in itertools.product(range(starting_index[0]-1, starting_index[0]+2), range(starting_index[1]-1, starting_index[1]+len(number)+1)):
        if (x,y) in symbols:
            part1+=int(number)
            break
submit(part1, part=1, day=day, year=year)

gears = {(x,y): list() for (x,y),z in symbols.items() if z=="*"}
for starting_index, number in numbers.items():
    for (x,y) in itertools.product(range(starting_index[0]-1, starting_index[0]+2), range(starting_index[1]-1, starting_index[1]+len(number)+1)):
        if (x,y) in gears:
            gears[(x,y)].append(int(number))
part2=sum([math.prod(list) for list in gears.values() if len(list)==2])
submit(part2, part=2, day=day, year=year)

