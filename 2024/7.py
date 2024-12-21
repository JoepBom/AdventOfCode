from aocd.models import Puzzle
from aocd import submit

year=2024
day=7
puzzle = Puzzle(year,day)

input = [(int(line.split(":")[0]), list(int(i) for i in line.split(":")[1].split() )) for line in puzzle.input_data.splitlines()]

def plus(a,b):
    return a+b

def times(a,b):
    return a*b

def concatenate(a,b):
    return int(str(a)+str(b))

def find_answer(input, operators):
    answer = 0
    for line in input:
        numbers = [line[1][0]]
        for i in range(1,len(line[1])):
            new_numbers = []
            for number in numbers:
                for operator in operators:
                    new_numbers.append(operator(number, line[1][i]))
            numbers = list(i for i in new_numbers if i<=line[0])
        if any((num == line[0] for num in numbers)):
            answer+=line[0]
    return answer
            

submit(find_answer(input, (plus, times)), part="a", day=day, year=year)
submit(find_answer(input, (plus, times, concatenate)), part="b", day=day, year=year)