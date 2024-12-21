from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
from math import gcd
from pprint import pprint
year=2024
day=10
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()
# input = puzzle.examples[-1].input_data.splitlines()

def get_scores1(input, trailend_dict_set,nr):
    new_trailend_dict_set = dict()
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] != nr:
                continue
            new_trailend_dict_set[(x,y)] = set()
            for x1, y1 in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if (x1,y1) in trailend_dict_set:
                    new_trailend_dict_set[(x,y)] = new_trailend_dict_set[(x,y)].union(trailend_dict_set[(x1,y1)])
    return new_trailend_dict_set

def get_scores2(input, trailend_dict_set,nr):
    new_trailend_dict_set = dict()
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] != nr:
                continue
            new_trailend_dict_set[(x,y)] = 0
            for x1, y1 in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if (x1,y1) in trailend_dict_set:
                    new_trailend_dict_set[(x,y)] += trailend_dict_set[(x1,y1)]
    return new_trailend_dict_set

trailend_dict_set1 = dict()
trailend_dict_set2 = dict()
for x in range(len(input)):
    for y in range(len(input[0])):
        if input[x][y] == "9":
            trailend_dict_set1[(x,y)] = set([(x,y)])
            trailend_dict_set2[(x,y)] = 1

for nr in range(8,-1,-1):
    trailend_dict_set1 = get_scores1(input, trailend_dict_set1, str(nr))
    trailend_dict_set2 = get_scores2(input, trailend_dict_set2, str(nr))
answer1 = sum([len(x) for x in trailend_dict_set1.values()])
answer2 = sum(x for x in trailend_dict_set2.values())
submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)
