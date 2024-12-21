from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
from math import gcd
from pprint import pprint
import re
year=2024
day=13
puzzle = Puzzle(year,day)

input = puzzle.input_data.split("\n\n")
# input = puzzle.examples[0].input_data.split("\n\n")

instances = []
for instance in input:
    lines = instance.splitlines()
    button_A = tuple(int(x) for x in re.findall(r'\d+', (lines[0])))
    button_B = tuple(int(x) for x in re.findall(r'\d+', (lines[1])))
    prize = tuple(int(x) for x in re.findall(r'\d+', (lines[2])))
    instances.append((button_A, button_B, prize))


def find_solution(button_A, button_B, prize):
    x_nom = button_A[0]*button_B[1]*prize[0] - button_A[0]*button_B[0]*prize[1]
    x_denom = button_A[0]*button_B[1] - button_A[1]*button_B[0]
    if x_nom % x_denom == 0:
        x = x_nom // x_denom
        if x%button_A[0] == 0 and (prize[0]-x)%button_B[0] == 0:
            return (x//button_A[0],(prize[0]-x)//button_B[0]), x//button_A[0]*3 + (prize[0]-x)//button_B[0]*1
    return None, 0

answer1=sum(sol for _,sol in (find_solution(instance[0], instance[1], instance[2]) for instance in instances))
answer2=sum(sol for _,sol in (find_solution(instance[0], instance[1], (instance[2][0]+10000000000000, instance[2][1]+10000000000000)) for instance in instances))

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)

