import numpy as np
import re
from pprint import pprint
import random
f = open("C:/Users/JoepBom/Documents/AdventOfCode/2022/19/input", "r")
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
    
    def get_max_ore(self):
        return max(self.ore_robot["ore"], self.clay_robot["ore"], self.obsidian_robot["ore"], self.geode_robot["ore"])
    

blueprints=[]
for nr, i in enumerate(input, 1):
    j = i.split(" ")
    blueprints.append(Blueprint(nr, [int(j[6]), int(j[12]), int(j[18]), int(j[21]), int(j[27]), int(j[30])]))


def get_next_states(bp: Blueprint, state: dict):
    new_states = []
    res = state.copy()
    res["time_left"]-=1
    res["ore"]+=res["ore_robots"]
    res["clay"]+=res["clay_robots"]
    res["obsidian"]+=res["obsidian_robots"]
    res["geode"]+=res["geode_robots"]
    if state["next_to_buy"]=="ore_robots" and state["ore"]>= bp.ore_robot["ore"]:
        res["ore"]-=bp.ore_robot["ore"]
        res["ore_robots"]+=1
        if res["ore_robots"]<bp.get_max_ore():
            res["next_to_buy"]="ore_robots"
            new_states.append(res)
        res1=res.copy()
        res1["next_to_buy"]="clay_robots"
        new_states.append(res1)
        res2=res.copy()
        if res2["clay_robots"]>0:
            res2["next_to_buy"]="obsidian_robots"
            new_states.append(res2)
        res3=res.copy()
        if res3["obsidian_robots"]>0:
            res3["next_to_buy"]="geode_robots"
            new_states.append(res3)
        return new_states
    if state["next_to_buy"]=="clay_robots" and state["ore"]>= bp.clay_robot["ore"]:
        res["ore"]-=bp.clay_robot["ore"]
        res["clay_robots"]+=1
        if res["ore_robots"]<bp.get_max_ore():
            res["next_to_buy"]="ore_robots"
            new_states.append(res)
        res0=res.copy()
        res0["next_to_buy"]="clay_robots"
        new_states.append(res0)
        res1=res.copy()
        res1["next_to_buy"]="obsidian_robots"
        new_states.append(res1)
        res2=res.copy()
        if res2["obsidian_robots"]>0:
            res2["next_to_buy"]="geode_robots"
            new_states.append(res2)
        return new_states
    if state["next_to_buy"]=="obsidian_robots" and state["ore"]>= bp.obsidian_robot["ore"] and state["clay"]>= bp.obsidian_robot["clay"]:
        res["ore"]-=bp.obsidian_robot["ore"]
        res["clay"]-=bp.obsidian_robot["clay"]
        res["obsidian_robots"]+=1
        if res["ore_robots"]<bp.get_max_ore():
            res["next_to_buy"]="ore_robots"
            new_states.append(res)
        res0=res.copy()
        res0["next_to_buy"]="clay_robots"
        new_states.append(res0)
        res1=res.copy()
        res1["next_to_buy"]="obsidian_robots"
        new_states.append(res1)
        res2=res.copy()
        res2["next_to_buy"]="geode_robots"
        new_states.append(res2)
        return new_states
    if state["next_to_buy"]=="geode_robots" and state["ore"]>= bp.geode_robot["ore"] and state["obsidian"]>= bp.geode_robot["obsidian"]:
        res["ore"]-=bp.geode_robot["ore"]
        res["obsidian"]-=bp.geode_robot["obsidian"]
        res["geode_robots"]+=1
        if res["ore_robots"]<bp.get_max_ore():
            res["next_to_buy"]="ore_robots"
            new_states.append(res)
        res0=res.copy()
        res0["next_to_buy"]="clay_robots"
        new_states.append(res0)
        res1=res.copy()
        res1["next_to_buy"]="obsidian_robots"
        new_states.append(res1)
        res2=res.copy()
        res2["next_to_buy"]="geode_robots"
        new_states.append(res2)
        return new_states
    return [res]


def evaluate_blueprint(bp: Blueprint):
    initial_state1 = {
        "time_left": 32,
        "ore_robots": 1,
        "clay_robots": 0,
        "obsidian_robots":0,
        "geode_robots": 0,
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
        "next_to_buy": "ore_robots"
        }
    initial_state2 = {
        "time_left": 32,
        "ore_robots": 1,
        "clay_robots": 0,
        "obsidian_robots":0,
        "geode_robots": 0,
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
        "next_to_buy": "clay_robots"
        }
    states=[initial_state1, initial_state2]
    final_states = []
    while states[0]["time_left"]>0:
        print(states[0]["time_left"], len(states))
        new_states = []
        for i in states:
            res=get_next_states(bp, i)
            for j in res:
                new_states.append(j)
        max_geode_potential = max(state["geode"]+state["time_left"]*state["geode_robots"] for state in new_states)
        states=[]
        for state in new_states:
            if state["geode"]+state["time_left"]*state["geode_robots"]+ int(state["time_left"]**2/2)>=max_geode_potential:
                states.append(state)
        
        # pprint(states)
        
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
        "geode": 0
        }
    for i in states:
        if i["geode"]> best_state["geode"]:
            best_state = i
    print(best_state)
    return best_state["geode"]
prod = 1
for count, i in enumerate(blueprints):
    if count<3:
        prod*=evaluate_blueprint(i)
    print(count)
print(f"Final answer: {prod}")

