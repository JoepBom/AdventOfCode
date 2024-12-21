from aocd.models import Puzzle
from aocd import submit
import re
year=2024
day=4
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()

def count_xmas1(input, x_dir, y_dir):
    counter = 0
    for x in range(0,len(input)):
        for y in range(0,len(input[0])):
            if (not (x+3*x_dir >= len(input) or x+3*x_dir < 0 or y+3*y_dir >= len(input[0]) or y+3*y_dir < 0) 
                and "".join([input[x+i*x_dir][y+i*y_dir] for i in range(4)])=="XMAS"):
                counter+=1
    return counter

def count_xmas2(input, x_dir, y_dir):
    counter = 0
    for x in range(0,len(input)):
        for y in range(0,len(input[0])):
            if (not (x+2*x_dir >= len(input) or x+2*x_dir < 0 or y+2*y_dir >= len(input[0]) or y+2*y_dir < 0) 
            and "".join([input[x+i*x_dir][y+i*y_dir] for i in range(3)])=="MAS" 
            and "".join([(input[x+(2-i)*x_dir][y+i*y_dir] if x_dir==y_dir else input[x+i*x_dir][y+(2-i)*y_dir]) for i in range(3)])=="MAS"):
                counter+=1
    return counter


answer1 = sum(count_xmas1(input,i,j) for i in range(-1,2) for j in range(-1,2) if i!=0 or j!=0)
answer2 = sum(count_xmas2(input,i,j) for i in range(-1,2) for j in range(-1,2) if i!=0 and j!=0)

print(answer1)
print(answer2)

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)