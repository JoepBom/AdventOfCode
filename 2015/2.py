import os
from aocd.models import Puzzle

os.environ['AOC_SESSION'] = '53616c7465645f5f1db1de03982a85cb67a3602dc24ea81710806a35b45ba3b2ee9f9dca5a807120d3602b8f6a017765b8d1266c375f0073f1c6e0889324856a'

year=2015
day=2
part='a'

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data

print(input.splitlines())
