from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint

year=2023
day=14
part="b"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()

rocks_by_x=list()
rocks_by_y=list()
balls_by_x=list()
balls_by_y=list()
for y, line in enumerate(input[::-1]):
    rocks_by_y.append(set())
    balls_by_y.append(set())
    for x, elem in enumerate(line):
        if y==0:
            rocks_by_x.append(set())
            balls_by_x.append(set())
        if elem=="O":
            balls_by_x[x].add(y)
            balls_by_y[y].add(x)
        if elem=="#":
            rocks_by_x[x].add(y)
            rocks_by_y[y].add(x)

max_y = len(balls_by_y)
max_x = len(balls_by_x)

def North(balls_by_x):
    balls_by_y=[set() for i in range(max_y)]
    for x in range(len(balls_by_x)):
        ball_count = 0
        new_balls_by_x=set()
        for y in range(len(balls_by_y)):
            if y in balls_by_x[x]:
                ball_count+=1
            if y in rocks_by_x[x]:
                if ball_count>0:
                    for i in range(1, ball_count+1):
                        new_balls_by_x.add(y-i)
                        balls_by_y[y-i].add(x)
                    ball_count=0
        if ball_count>0:
            for i in range(len(balls_by_y)-ball_count, len(balls_by_y)):
                new_balls_by_x.add(i)
                balls_by_y[i].add(x)
        balls_by_x[x]=new_balls_by_x
    return (balls_by_x, balls_by_y)

def South(balls_by_x):
    balls_by_y=[set() for i in range(max_y)]
    for x in range(len(balls_by_x)):
        ball_count = 0
        new_balls_by_x=set()
        for y in range(len(balls_by_y)-1, -1, -1):
            if y in balls_by_x[x]:
                ball_count+=1
            if y in rocks_by_x[x]:
                if ball_count>0:
                    for i in range(1, ball_count+1):
                        new_balls_by_x.add(y+i)
                        balls_by_y[y+i].add(x)
                    ball_count=0
        if ball_count>0:
            for i in range(0, ball_count):
                new_balls_by_x.add(i)
                balls_by_y[i].add(x)
        balls_by_x[x]=new_balls_by_x
    return (balls_by_x, balls_by_y)

def East(balls_by_y):
    balls_by_x=[set() for i in range(max_x)]
    for y in range(len(balls_by_y)):
        ball_count = 0
        new_balls_by_y=set()
        for x in range(len(balls_by_x)):
            if x in balls_by_y[y]:
                ball_count+=1
            if x in rocks_by_y[y]:
                if ball_count>0:
                    for i in range(1, ball_count+1):
                        new_balls_by_y.add(x-i)
                        balls_by_x[x-i].add(y)
                    ball_count=0
        if ball_count>0:
            for i in range(len(balls_by_x)-ball_count, len(balls_by_x)):
                new_balls_by_y.add(i)
                balls_by_x[i].add(y)
        balls_by_y[y]=new_balls_by_y
    return (balls_by_x, balls_by_y)

def West(balls_by_y):
    balls_by_y=balls_by_y
    balls_by_x=[set() for i in range(max_x)]
    for y in range(len(balls_by_y)):
        ball_count = 0
        new_balls_by_y=set()
        for x in range(len(balls_by_x)-1, -1, -1):
            if x in balls_by_y[y]:
                ball_count+=1
            if x in rocks_by_y[y]:
                if ball_count>0:
                    for i in range(1, ball_count+1):
                        new_balls_by_y.add(x+i)
                        balls_by_x[x+i].add(y)
                    ball_count=0
        if ball_count>0:
            for i in range(0, ball_count):
                new_balls_by_y.add(i)
                balls_by_x[i].add(y)
        balls_by_y[y]=new_balls_by_y
    return (balls_by_x, balls_by_y)

def Cycle(balls_by_x):
    return East(South(West(North(balls_by_x)[1])[0])[1])[0]

def print_balls(balls_by_x_old):
    for y in range(len(balls_by_y)-1,-1,-1):
        for x in range(len(balls_by_x_old)):
            if y in balls_by_x_old[x]:
                print("O", end="")
            elif y in rocks_by_x[x]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def check_if_same(balls_by_x_old, balls_by_x2):
    for i, balls_by_x1 in enumerate(balls_by_x_old):
        same=True
        for set1, set2 in zip(balls_by_x1,balls_by_x2):
            if len(set1 - set2) != 0 or len(set2 - set1) != 0:
                same=False
                break
        if same:
            return i
    return 0

balls_by_x_old=[]

count=0
while not check_if_same(balls_by_x_old, balls_by_x):
    balls_by_x_old.append(balls_by_x.copy())
    balls_by_x=Cycle(balls_by_x)
    count+=1

loop_start = check_if_same(balls_by_x_old, balls_by_x)
print_balls(balls_by_x_old[loop_start])
print_balls(balls_by_x)
print(count)
print(loop_start)

loop_length = count-loop_start

balls_by_x = balls_by_x_old[((1000000000-loop_start)%loop_length)+loop_start]

balls_by_y=[set() for i in range(max_y)]
for x in range(len(balls_by_x)):
    for y in balls_by_x[x]:
        balls_by_y[y].add(x)
print(sum((1+y)*len(balls_by_y[y]) for y in range(len(balls_by_y))))
submit(sum((1+y)*len(balls_by_y[y]) for y in range(len(balls_by_y))), part=part, day=day, year=year)