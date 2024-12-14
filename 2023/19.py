from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint


year=2023
day=19
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

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

print(sol1)



submit(sol1, part=part, day=day, year=year)

part="b"


interesting_values = {"x": {0, 4000}, "m": {0, 4000}, "a": {0, 4000}, "s": {0, 4000}}

for job_id, job in job_dict.items():
    for test in job.tests[:-1]:
        interesting_values[test[0]].add(int(test[2:]))
        if test[1]=="<":
            interesting_values[test[0]].add(int(test[2:])-1)
        else:
            interesting_values[test[0]].add(int(test[2:])+1)

interesting_values={key: sorted(val) for key,val in interesting_values.items()}
# pprint(interesting_values)
sol2=0
for xi, x in enumerate(interesting_values["x"][1:]):
    try:
        if eval_input({"x": x}):
            sol2+=(x-interesting_values["x"][xi])*4000**3
        continue
    except:
         None
    for mi, m in enumerate(interesting_values["m"][1:]):
        try:
            if eval_input({"x": x, "m": m}):
                sol2+=(x-interesting_values["x"][xi])*(m-interesting_values["m"][mi])*4000**2
            continue
        except:
            None
        for ai, a in enumerate(interesting_values["a"][1:]):
            try:
                if eval_input({"x": x, "m": m, "a":a}):
                    sol2+=(x-interesting_values["x"][xi])*(m-interesting_values["m"][mi])*(a-interesting_values["a"][ai])*4000
                continue
            except:
                None  
            for si, s in enumerate(interesting_values["s"][1:]):
                if eval_input({"x": x, "m": m, "a":a, "s":s}):
                    sol2+= (x-interesting_values["x"][xi])*(m-interesting_values["m"][mi])*(a-interesting_values["a"][ai])*(s-interesting_values["s"][si])

print(sol2)

submit(sol2, part=part, day=day, year=year)
