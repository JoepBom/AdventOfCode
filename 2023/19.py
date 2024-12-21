from typing import Dict, Tuple
from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint


year=2023
day=19
part="a"

puzzle = Puzzle(year,day)
input = puzzle.input_data
workflows = input.split("\n\n")[0].splitlines()
input =input.split("\n\n")[1].splitlines()
pprint(workflows)

class Job:
    tests: list
    next_steps: list
    id: str

    def __init__(self, line) -> None:
        self.id = line.split("{")[0]
        test_list = line.split("{")[1][:-1].split(",")
        self.next_steps=[]
        self.tests=[]
        for test in test_list[:-1]:
            self.next_steps.append(test.split(":")[-1])
            self.tests.append(test.split(":")[0])
        self.tests.append("")
        self.next_steps.append(test_list[-1])

    def eval_job(self, val_dict):
        for i, test in enumerate(self.tests[:-1]):
            var= test[0]
            amount = int(test[2:])
            if test[1]==">" and val_dict[var]>amount:
                return self.next_steps[i]
            elif test[1]=="<" and val_dict[var]<amount:
                return self.next_steps[i]
        return self.next_steps[-1]
    


job_dict=dict()
for workflow in workflows:
    job = Job(workflow)
    job_dict[job.id]=job



sol1=0
def eval_input(val_dict):
    accepted = None
    job_id = "in"
    # print()
    # print(val_dict)
    while accepted is None:
        res = job_dict[job_id].eval_job(val_dict)
        if res == "A":
            accepted = True
        elif res == "R":
            accepted = False
        else:
            job_id = res
    if accepted:
        return True
    return False

for line in input:
    val_dict = dict()
    value_lines = line[1:-1].split(",")
    for value_line in value_lines:
        val_dict[value_line.split("=")[0]]= int(value_line.split("=")[1])
    if eval_input(val_dict):
        sol1+=sum(val_dict.values())

# print(sol1)



# submit(sol1, part=part, day=day, year=year)

part="b"


ranges = {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}

def get_range_combinations(range_dict: Dict[str, Tuple[int]]):
    lengths = [range_dict[key][1]-range_dict[key][0] for key in range_dict]
    return lengths[0]*lengths[1]*lengths[2]*lengths[3]

def evaluate_range(range_dict: Dict[str, Tuple[int]], job_dict: Dict[str, Job], job_id: str, test_nr: int):
    test = job_dict[job_id].tests[test_nr]
    next_step = job_dict[job_id].next_steps[test_nr]
    if len(test)==0:
        if next_step == "A":
            return get_range_combinations(range_dict)
        if next_step == "R":
            return 0
        return evaluate_range(range_dict, job_dict, next_step, 0)
    var= test[0]
    amount = int(test[2:])
    correct_range_dict = None
    false_range_dict = None
    if test[1]==">":
        if amount in range(range_dict[var][0], range_dict[var][1]-1):
            correct_range_dict = range_dict.copy()
            correct_range_dict[var] = (amount+1, range_dict[var][1])
            false_range_dict = range_dict.copy()
            false_range_dict[var] = (range_dict[var][0], amount+1)
        elif amount < range_dict[var][0]:
            correct_range_dict = range_dict.copy()
        else:
            false_range_dict = range_dict.copy()
    elif test[1]=="<":
        if amount in range(range_dict[var][0]+1, range_dict[var][1]):
            correct_range_dict = range_dict.copy()
            correct_range_dict[var] = (range_dict[var][0], amount)
            false_range_dict = range_dict.copy()
            false_range_dict[var] = (amount, range_dict[var][1])
        elif amount > range_dict[var][1]:
            correct_range_dict = range_dict.copy()
        else:
            false_range_dict = range_dict.copy()
    res = 0
    if correct_range_dict is not None:
        if next_step == "A":
            res += get_range_combinations(correct_range_dict)
        elif next_step != "R":
            res += evaluate_range(correct_range_dict, job_dict, next_step, 0)
    if false_range_dict is not None:
        res += evaluate_range(false_range_dict, job_dict, job_id, test_nr+1)
    return res

sol2 = evaluate_range(ranges, job_dict, "in", 0)
print(sol2)

submit(sol2, part=part, day=day, year=year)
