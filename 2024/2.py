from aocd.models import Puzzle
from aocd import submit

year=2024
day=2
puzzle = Puzzle(year,day)

lines = puzzle.input_data.splitlines()
answer1 = 0
answer2 = 0
for line in lines:
    levels = line.split()
    for i in range(len(levels)):
        differences = [int(levels[i]) - int(levels[i-1]) for i in range(1,len(levels))]
        if (
            (all([d > 0 for d in differences]) or all([d<0 for d in differences])) 
            and all([1 <= abs(d) and abs(d) <= 3 for d in differences])
        ):
            answer1 += 1
        levels_2 = levels.copy()
        levels_2.pop(i)
        differences = [int(levels_2[i]) - int(levels_2[i-1]) for i in range(1,len(levels_2))]
        if ((
            all([d > 0 for d in differences]) or all([d<0 for d in differences]))
            and all([1 <= abs(d) and abs(d) <= 3 for d in differences])
        ):
            answer2 += 1
            break

submit(answer1, part=1, day=day, year=year)
submit(answer2, part=2, day=day, year=year)