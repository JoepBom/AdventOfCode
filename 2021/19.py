
from aocd.models import Puzzle
from aocd import submit

import os

os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"
puzzle = Puzzle(2021,19)

print(puzzle.input_data)

# print(puzzle.)