from aocd.models import Puzzle
from aocd import submit
import os
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

year=2023
day=9
part="a"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()

ans1=0
for line in input:
    values = [int(i) for i in line.split()]
    while len(values)>1:
        ans1+=values[-1]
        values=[values[i]-values[i-1] for i in range(1,len(values))]

submit(ans1, part=part, year=year, day=day)

part="b"

ans2=0
for line in input:
    first_vals = []
    values = [int(i) for i in line.split()]
    while True:
        first_vals.append(values[0])
        values=[values[i]-values[i-1] for i in range(1,len(values))]
        if not any(values):
            break
    sol=0
    for val in first_vals[::-1]:
        sol=val-sol
    ans2+=sol

submit(ans2, part=part, year=year, day=day)