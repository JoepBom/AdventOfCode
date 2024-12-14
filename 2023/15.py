from aocd.models import Puzzle
from aocd import submit
import os
import re
year=2023
day=15
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.split(",")

def HashAlg(i):
    curVal = 0
    for j in i:
        curVal+=ord(j)
        curVal*=17
        curVal=curVal % 256
    return curVal

sol1=0
for i in input:
    sol1+=HashAlg(i)

submit(sol1, part=part, day=day, year=year)

part="b"

boxes = {i: list() for i in range(256)}

for instr in input:
    label = re.split(r"-|=", instr)[0]
    boxNr = HashAlg(label)
    eq_index = instr.find("=")
    if eq_index==-1:
        for i, lens in enumerate(boxes[boxNr]):
            if lens[0] == label:
                boxes[boxNr].pop(i)
        continue
    replaced=False
    for i, lens in enumerate(boxes[boxNr]):
        if lens[0] == label:
            lens[1]=int(instr[eq_index+1:])
            replaced=True
            break
    if not replaced:
        boxes[boxNr].append([label, int(instr[eq_index+1:])])

sol2=0
for boxNr, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        sol2+=lens[1]*(i+1)*(boxNr+1)

submit(sol2, part=part, day=day, year=year)