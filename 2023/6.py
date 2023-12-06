import os
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint
import re
import math
os.environ['AOC_SESSION'] = '53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d'

year=2023
day=6

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()

pprint(input)
times = [int(i) for i in re.split(r"\s{1,10}", input[0])[1:]]
distances = [int(i) for i in re.split(r"\s{1,10}", input[1])[1:]]

sol1=1
for time, distance in zip(times, distances):
    lower_bound = int((time - math.sqrt(time**2-4.*distance))/2)
    upper_bound = int((time + math.sqrt(time**2-4.*distance))/2)
    sol1*=upper_bound-lower_bound

submit(sol1, part = 1, year=year, day=day)

# concatenate all numbers from input[0] and input[1] into one string
time = int(input[0].replace(" ","")[5:])
distance = int(input[1].replace(" ","")[9:])

lower_bound = int((time - math.sqrt(time**2-4.*distance))/2)
upper_bound = int((time + math.sqrt(time**2-4.*distance))/2)
print(lower_bound, upper_bound)
sol2=upper_bound-lower_bound

submit(sol2, part=2, year=year, day=day)

    