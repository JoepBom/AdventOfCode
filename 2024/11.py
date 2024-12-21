from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
from math import gcd
from pprint import pprint
year=2024
day=11
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()[0].split()
# input = puzzle.examples[0].input_data.splitlines()[1].split()
print(input)

stone_dict = dict()
for stone in input:
    stone_dict[stone] = 1

def add_stones(stone_dict, stone, amount):
    if stone not in stone_dict:
        stone_dict[stone] = 0
    stone_dict[stone] += amount
    return

count=0
while True:
    new_stone_dict = dict()
    for stone, val in stone_dict.items():
        if stone == "0":
            add_stones(new_stone_dict, "1", val)
        elif len(stone)%2 == 0:
            new_stones = (str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):])))
            add_stones(new_stone_dict, new_stones[0], val)
            add_stones(new_stone_dict, new_stones[1], val)
        else:
            add_stones(new_stone_dict, str(int(stone)*2024), val)
    stone_dict = new_stone_dict
    count+=1
    if count == 25:
        answer1 = sum(stone_dict.values())
    if count == 75:
        answer2 = sum(stone_dict.values())
        break

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)