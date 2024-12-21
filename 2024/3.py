from aocd.models import Puzzle
from aocd import submit
import re
year=2024
day=3
puzzle = Puzzle(year,day)

mul_list = re.findall(r"(do(?:n't)?\(\))|mul\((\d{1,3},\d{1,3})\)", puzzle.input_data)

answer1 = 0
answer2 = 0
do=True
for does, mul in mul_list:
    if does == "do()":
        do = True
    elif does == "don't()":
        do = False
    elif do:
        answer2 += int(mul.split(",")[0])*int(mul.split(",")[1])
    if mul:
        answer1+=int(mul.split(",")[0])*int(mul.split(",")[1])

submit(answer1, part=1, day=day, year=year)
submit(answer2, part=2, day=day, year=year)