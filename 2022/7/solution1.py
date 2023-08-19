import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/7/input.txt", "r")
input = f.read().splitlines()
print(input)

class Directory:
    'class for directory objects'
    name: str
    files: dict
    dirs: dict
    prev: object
    def __init__(self, prev, name) -> None:
        self.name = name
        self.files = dict()
        self.dirs = dict()
        if prev is not None:
            self.prev = prev
            prev.add_directory(self)
        else:
            prev = None
    def add_file(self, name, size):
        self.files[name] = size
    def add_directory(self, dir):
        self.dirs[dir.name] = dir
    def get_dir_size(self):
        tot = 0
        tot_sizes = list()
        for file_size in self.files.values():
            tot+=file_size
        for dir in self.dirs.values():
            size, sizes = dir.get_dir_size()
            tot+= size
            for size in sizes:
                tot_sizes.append(size)
        tot_sizes.append(tot)
        print(tot)
        print(tot_sizes)
        return tot, tot_sizes

main_dir = None
cur_dir = None
for line in input:
    print(line)
    if line[:4] == "$ cd":
        #moving directories
        if line[5:] == "..":
            #move back
            cur_dir = cur_dir.prev
        elif line[5:] == "/":
            #move to start
            if main_dir is None:
                main_dir = Directory(None, "/")
            cur_dir = main_dir                
        else:
            #move forward
            name = line[5:]
            if name in cur_dir.dirs.keys():
                cur_dir = cur_dir.dirs[name]
            else:
                #create new, set as cur_dir
                cur_dir = Directory(cur_dir, name)
    elif line == "$ ls":
        continue
    else:
        #we have a file or dir
        input1, input2 = line.split(" ")
        if input1 == "dir":
            cur_dir.add_directory(Directory(cur_dir, input2))
        else:
            cur_dir.add_file(input2, int(input1))

tot, sizes = main_dir.get_dir_size()
sum = 0
for size in sizes:
    if size<= 100000:
        sum+=size
print(sum)

options = list()
for size in sizes:
    if size>=30000000 - (70000000 - tot):
        options.append(size)
print(min(options))


    
