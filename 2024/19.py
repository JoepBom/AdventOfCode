from aocd.models import Puzzle
from aocd import submit

year=2024
day=19
puzzle = Puzzle(year,day)

input = puzzle.input_data.split("\n\n")
towels = input[0].split(", ")
designs = input[1].splitlines()

possible_designs = dict()
def count_possible(design):
    if design in possible_designs:
        return possible_designs[design]
    possible_designs[design] = int(design in towels)
    for i in range(1, len(design)):
        if design[i:] in towels:
            possible_designs[design]+=count_possible(design[:i])
    return possible_designs[design]

answer1=0
answer2=0
for design in designs:
    options = count_possible(design) 
    answer1 += int(bool(options))
    answer2 += options

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)