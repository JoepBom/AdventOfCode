from aocd.models import Puzzle
from aocd import submit
import os

year=2023
day=2
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data

Games = dict()
for line in input.splitlines():
    id, game = line.split(": ")
    Games[id]={"red":[], "green":[], "blue":[]}
    for round in game.split("; "):
        for element in round.split(","):
            amount, color = element.split()
            Games[id][color].append(int(amount))

sum=0
for id, Game in Games.items():
    if max(Game["red"])>12 or max(Game["green"])>13 or max(Game["blue"])>14:
        continue        
    sum+= int(id.split()[1])
submit(sum, part=1, day=day, year=year)

sum=0
for id, Game in Games.items():
    power=max(Game["red"])*max(Game["green"])*max(Game["blue"])
    sum+= power
submit(sum, part=2, day=day, year=year)