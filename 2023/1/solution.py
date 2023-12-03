from aocd.models import Puzzle
from aocd import submit
import os
import re 

year=2023
day=1
os.environ["AOC_SESSION"]="53616c7465645f5f5fc04372cc4a1e43a82fc9730ef3d0613d407fc8357e36f0b765d4fd98bf9fc1b557f8305d9028761328b7270887ebf465683171f2b8b14d"

puzzle = Puzzle(year,day)
input1 = re.sub(r"[a-z]", "", puzzle.input_data).splitlines()
replacements = {"one": "on1ne", 
                "two": "tw2wo", 
                "three": "thre3hree", 
                "four": "fou4our", 
                "five": "fiv5ive", 
                "six": "si6ix",
                "seven": "seve7even",
                "eight": "eigh8ight",
                "nine": "nin9ine"}
input2 = puzzle.input_data
for nr, repl in replacements.items():
    input2 = re.sub(nr, repl, input2)
input2 = re.sub(r"[a-z]", "", input2).splitlines()
answer1=sum(int(i[0]+i[-1]) for i in input1)
answer2=sum(int(i[0]+i[-1]) for i in input2)

submit(answer1, part=1, day=day, year=year)
submit(answer2, part=2, day=day, year=year)