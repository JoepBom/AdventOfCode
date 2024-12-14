from aocd.models import Puzzle
from aocd import submit
import os

year=2023
day=13
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.split("\n\n")
input = [[line for line in input1.splitlines()] for input1 in input]

sol1=0
for grid in input:
    for x_line in range(1, len(grid)):
        found = True
        smudge = False
        for x in range(0, x_line):
            x2 = 2 * x_line - x -1
            if x2 >= len(grid):
                continue
            boolarray = [grid[x][i]!=grid[x2][i] for i in range(len(grid[x]))]
            if any(boolarray):
                if not smudge and sum(boolarray)==1:
                    smudge=True
                    continue
                found=False
                break
        if found and smudge:
            sol1+=100*x_line
            break
    for y_line in range(1, len(grid[0])):
        found = True
        smudge = False
        for y in range(0, y_line):
            y2 = 2*y_line - y - 1
            if y2 >= len(grid[0]):
                continue
            boolarray=[grid[i][y]!=grid[i][y2] for i in range(len(grid))]
            if any(boolarray):
                if not smudge and sum(boolarray)==1:
                    smudge=True
                    continue
                found=False
                break
        if found and smudge:
            sol1+=y_line
            break

submit(sol1, year=year, part="b", day=day)

