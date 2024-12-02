from aocd.models import Puzzle
from aocd import submit

year=2024
day=1
puzzle = Puzzle(year,day)

x = sorted(int(line.split()[0]) for line in puzzle.input_data.splitlines())
y = sorted(int(line.split()[-1]) for line in puzzle.input_data.splitlines())
answer1 = sum([abs(x[i]-y[i]) for i in range(len(x))])
answer2 = sum([num*y.count(num) for num in set(x).intersection(set(y))])

submit(answer1, part=1, day=day, year=year)
submit(answer2, part=2, day=day, year=year)