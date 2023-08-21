import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/19/input_small", "r")
input = f.read().splitlines()
class Blueprint:
    number: int
    ore_robot: dict()
    clay_robot: dict()
    obsidian_robot: dict()
    geode_robot: dict()

    def __init__(self, number, numbers) -> None:
        self.number=number
        self.ore_robot={"ore": numbers[0]}
        self.clay_robot={"ore": numbers[1]}
        self.obsidian_robot={"ore": numbers[2], "clay": numbers[3]}
        self.geode_robot={"ore": numbers[4], "obsidian": numbers[5]}
    
blueprints=[]
for nr, i in enumerate(input, 1):
    j = i.split(" ")
    blueprints.append(Blueprint(nr, [int(j[6]), int(j[12]), int(j[18]), int(j[21]), int(j[27]), int(j[30])]))




def compare_states(state1, state2):
    state1_win = True
    state2_win = True
    for key in state1.keys():
        if key in {"time_left", "buying"}:
            continue
        if state1[key]> state2[key]:
            state2_win = False
        if state1[key]< state2[key]:
            state1_win = False
    if state1_win == state2_win:
        return None
    if state1_win:
        return 0
    if state2_win:
        return 1

def get_possible_states(bp: Blueprint, state: dict):
    new_states = []
    if state["ore"]>= bp.ore_robot["ore"]:
        res = state.copy()
        res["buying"]="ore_robots"
        res["ore"]-=bp.ore_robot["ore"]
        new_states.append(res)
    if state["ore"]>= bp.clay_robot["ore"]:
        res = state.copy()
        res["buying"]="clay_robots"
        res["ore"]-=bp.clay_robot["ore"]
        new_states.append(res)    
    if state["ore"]>= bp.obsidian_robot["ore"] and state["clay"]>= bp.obsidian_robot["clay"]:
        res = state.copy()
        res["buying"]="obsidian_robots"
        res["ore"]-=bp.obsidian_robot["ore"]
        res["clay"]-=bp.obsidian_robot["clay"]
        new_states.append(res) 
    if state["ore"]>= bp.geode_robot["ore"] and state["obsidian"]>= bp.geode_robot["obsidian"]:
        res = state.copy()
        res["buying"]="geode_robots"
        res["ore"]-=bp.geode_robot["ore"]
        res["obsidian"]-=bp.geode_robot["obsidian"]
        new_states.append(res)
    res = state.copy()
    res["buying"]=None
    new_states.append(res)    
    for i in new_states:
        i["time_left"]-=1
        i["ore"]+=i["ore_robots"]
        i["clay"]+=i["clay_robots"]
        i["obsidian"]+=i["obsidian_robots"]
        i["geode"]+=i["geode_robots"]
        if i["buying"] is not None:
            i[i["buying"]]+=1
    return new_states

def evaluate_blueprint(bp: Blueprint):
    initial_state = {
        "time_left": 24,
        "ore_robots": 1,
        "clay_robots": 0,
        "obsidian_robots":0,
        "geode_robots": 0,
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
        "buying": None
        }
    states=[initial_state]
    final_states = []
    while len(states)>0:
        print(len(states))
        new_states = []
        for i in states:
            if i["time_left"]==0:
                final_states.append(i)
                continue
            res=get_possible_states(bp, i)
            for j in res:
                to_remove=[]
                add = True
                if len(new_states)<2000:
                    for k in new_states:
                        res=compare_states(j,k)
                        if res is None:
                            continue
                        if res==1:
                            add = False
                            break
                        if res==0:
                            to_remove.append(k)
                    for k in to_remove:
                        new_states.remove(k)
                if add:
                    new_states.append(j)
        states = new_states
    print("done")
    best_state={
        "time_left": 0,
        "ore_robots": 0,
        "clay_robots": 0,
        "obsidian_robots":0,
        "geode_robots": 0,
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
        "buying": None
        }
    for i in final_states:
        if i["geode"]> best_state["geode"]:
            best_state = i
    print(best_state)
    return best_state["geode"]*bp.number

print(f"Final answer: {sum(evaluate_blueprint(i) for i in blueprints)}")












