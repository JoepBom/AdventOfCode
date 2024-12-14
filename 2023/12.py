from aocd.models import Puzzle
from aocd import submit
import os
import re
from pprint import pprint
year=2023
day=12
part="b"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()
# input = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".splitlines()
lines = []
for line in input:
    lines.append([re.sub("\.\.", ".", line.split(" ")[0]), [int(i) for i in line.split(" ")[1].split(",")]])

lines2= []
for thing in lines:
    lines2.append([thing[0]+"?"+thing[0]+"?"+thing[0]+"?"+thing[0]+"?"+thing[0], thing[1]+thing[1]+thing[1]+thing[1]+thing[1]])

def evaluate_line2(line, instr):
    res=0
    for i in range(len(line)-instr[0]+1):
        if "#" in line[:i]:
            break
        if "." in line[i:i+instr[0]]:
            continue
        if len(line)>i+instr[0] and line[i+instr[0]] == "#":
            continue
        if len(instr)==1:
            if "#" in line[i+instr[0]:]:
                continue
            res+=1
            continue
        res+=evaluate_line2(line[i+instr[0]+1:], instr[1:])
    return res


# def trim_line(line, instr):
#     if len(line)==0 or len(instr)==0:
#         return "", []
#     while line[0]==".":
#         line=line[1:]
#     if len(line)==sum(instr)+len(instr)-1:
#         return "", []
#     if line[0]=="#" or ("#" in list(line[:instr[0]]) and line[instr[0]]=="."):
#         line=line[(instr[0]+1):]
#         instr=instr[1:]
#         return line, instr
#     if line[instr[0]]=="#":
#         line=line[1:]
#     return line, instr

# trimmed_lines = []
# for thing in lines:
#     line=[]
#     instr=thing[1]
#     new_line=thing[0]
#     while len(new_line)!=len(line) and len(new_line)!=0:
#         line=new_line
#         new_line, instr = trim_line(line,instr)
#         instr.reverse()
#         new_line, instr = trim_line(new_line[::-1], instr)
#     trimmed_lines.append([new_line, instr])

def evaluate_line(line, instr):
    options_to_check = len(line) - (sum(instr)+len(instr)-1)+1
    options={i: dict() for i in range(len(instr))}
    if len(instr) == 0:
        return 1
    for start_spot in range(options_to_check):
        if not "#" in line[:start_spot] and not "." in line[start_spot:start_spot+instr[0]] and not ((len(line)>start_spot+instr[0] and line[start_spot+instr[0]]=="#")):
            options[0][start_spot] = 1
    if len(instr) == 1:
        return sum(options[0].values())
    for i, length in enumerate(instr[1:], 1):
        min_start_spot = sum(instr[:i])+i
        for start_spot in range(min_start_spot, min_start_spot+options_to_check):
            if "#"==line[start_spot-1] or "." in line[start_spot:start_spot+length] or ((len(line)>start_spot+length and line[start_spot+length]=="#")):
                continue
            if i==len(instr)-1 and len(line)>start_spot+length and "#" in line[start_spot+length:]:
                continue
            # Valid location
            count=0
            for prev_start_spot, prev_count in options[i-1].items():
                if prev_start_spot+instr[i-1]>=start_spot:
                    continue
                if "#" in line[prev_start_spot+instr[i-1]:start_spot]:
                    continue
                count+=prev_count
            if count>0:
                options[i][start_spot]=count
    return sum(options[len(instr)-1].values())

sol1=0
for i, line in enumerate(lines):
    sol1+=evaluate_line(line[0], line[1])

print(sol1)
    


submit(sol1, part="a", day=day, year=year)


sol2=0
for i, line in enumerate(lines2):
    sol2+=evaluate_line(line[0], line[1])

submit(sol2, part="b", day=day, year=year)