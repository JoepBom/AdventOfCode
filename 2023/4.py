import os
from aocd.models import Puzzle
import aocd
import re
os.environ['AOC_SESSION'] = '53616c7465645f5f5274298a1513bd33b311098204a4e371d2880a4590e8a95748ea42877f6b28b349045dcc1fee6d10f00932890ec53d2fdfe8a068bae08242'

year=2023
day=4

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()

Cards=[]
for line in input:
    i = re.split(r":|\|", line)
    Cards.append([set(i[1].split()), set(i[2].split())])
ans1=sum((2**len(i[0] & i[1])//2 for i in Cards))
aocd.submit(answer=ans1, year=year, day=day, part=1)

amounts = [1]*len(Cards)
for i, card in enumerate(Cards):
    for j in range(len(card[0] & card[1])):
        if i+1+j < len(amounts):
            	amounts[i+1+j] += amounts[i]
ans2 = sum(amounts)

aocd.submit(answer=ans2, year=year, day=day, part=2)