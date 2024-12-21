from aocd.models import Puzzle
from aocd import submit
import re

year=2024
day=17
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()
# input = puzzle.examples[0].input_data.splitlines()

def int_to_bin_list(A_int):
    A_bin = list()
    count = 1
    while True:
        if A_int == 0:
            break
        if A_int%(2*count) == 0:
            A_bin.append(0)
        else:
            A_bin.append(1)
            A_int -= count
        count *= 2
    return A_bin

def bin_list_to_int(A_bin):
    A_int = 0
    for i, bit in enumerate(A_bin):
        A_int += bit*(2**i)
    return A_int

def div(register, value):
    if len(register)< value:
        return []
    return register[value:]

def xor(register: list, bin_list: list):
    res = list()
    for i in range(max(len(register), len(bin_list))):
        res.append(
            ((register[i] if i<len(register) else 0) + (bin_list[i] if i<len(bin_list) else 0))%2
        )
    return res

class Computer():

    A_reg: list
    B_reg: list
    C_reg:list
    output: list

    def __init__(self, A_int, B_int, C_int):
        if type(A_int) == list:
            self.A_reg = A_int
        else:
            self.A_reg = int_to_bin_list(A_int)
        self.B_reg = int_to_bin_list(B_int)
        self.C_reg = int_to_bin_list(C_int)
        self.output = list()
        pass


    def combo(self, operand):
        if operand == 4:
            return self.A_reg
        if operand == 5:
            return self.B_reg
        if operand == 6:
            return self.C_reg
        return operand

    def bst(self, operand):
        literal = self.combo(operand)
        if type(literal) == int:
            literal = int_to_bin_list(literal)
        self.B_reg = literal[:3]
        return

    def jnz(self, operand):
        if len(self.A_reg) == 0:
            return -1
        return operand

    def out(self, operand):
        literal = self.combo(operand)
        if type(literal) == int:
            literal = int_to_bin_list(literal)
        self.output.append(bin_list_to_int(literal[:3]))
        return

    def adv(self, operand):
        literal = self.combo(operand)
        if type(literal) == list:
            literal = bin_list_to_int(literal)
        self.A_reg = div(self.A_reg, literal)
        return

    def bdv(self, operand):
        literal = self.combo(operand)
        if type(literal) == list:
            literal = bin_list_to_int(literal)
        self.B_reg = div(self.A_reg, literal)
        return

    def cdv(self, operand):
        literal = self.combo(operand)
        if type(literal) == list:
            literal = bin_list_to_int(literal)
        self.C_reg = div(self.A_reg, literal)
        return

    def bxl(self, operand):
        literal = int_to_bin_list(operand)
        self.B_reg=xor(self.B_reg, literal)
        return

    def bxc(self, operand):
        self.B_reg=xor(self.B_reg, self.C_reg)
        return



A_int = int(input[0].split()[-1])
B_int = int(input[1].split()[-1])
C_int = int(input[2].split()[-1])
print(input)
Program = [int(i) for i in input[4].split()[-1].split(",")]
print(Program)
# A_int = 2024
# B_int = 2024
# C_int = 43690

# Program = [4,0]


comp = Computer(A_int, B_int, C_int)

pointer = 0
while True:
    if pointer >= len(Program):
        break
    if Program[pointer] == 0:
        comp.adv(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 1:
        comp.bxl(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 2:
        comp.bst(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 3:
        res = comp.jnz(Program[pointer+1])
        if res != -1:
            pointer = res
        else:
            pointer+=2
        continue
    if Program[pointer] == 4:
        comp.bxc(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 5:
        comp.out(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 6:
        comp.bdv(Program[pointer+1])
        pointer+=2
        continue
    if Program[pointer] == 7:
        comp.cdv(Program[pointer+1])
        pointer+=2
        continue

print(comp.output)

answer1 = ",".join([str(i) for i in comp.output])

print(answer1)
submit(answer1, part="a", day=day, year=year)


def check_options(A_bin, program_subset):
    print(f"Checking: {A_bin}")
    while len(A_bin)>0 and A_bin[-1] == 0:
        A_bin = A_bin[:-1]
    
    if len(A_bin) == 0:
        return None
    comp = Computer(A_bin, B_int, C_int)
    pointer = 0
    Searching = True
    while Searching:
        if pointer >= len(Program):
            if len(comp.output)<len(program_subset):
                Searching = False
            break
        if Program[pointer] == 0:
            comp.adv(Program[pointer+1])
            pointer+=2
            continue
        if Program[pointer] == 1:
            comp.bxl(Program[pointer+1])
            pointer+=2
            continue
        if Program[pointer] == 2:
            comp.bst(Program[pointer+1])
            pointer+=2
            continue
        if Program[pointer] == 3:
            res = comp.jnz(Program[pointer+1])
            if res != -1:
                pointer = res
            else:
                pointer+=2
            continue
        if Program[pointer] == 4:
            comp.bxc(Program[pointer+1])
            pointer+=2
            continue
        if Program[pointer] == 5:
            comp.out(Program[pointer+1])
            pointer+=2
            print(comp.output)
            print(program_subset)
            for i,x in enumerate(comp.output):
                if x != program_subset[i]:
                    Searching = False
                    break
            continue
        if Program[pointer] == 6:
            comp.bdv(Program[pointer+1])
            pointer+=2
            continue
        if Program[pointer] == 7:
            comp.cdv(Program[pointer+1])
            pointer+=2
            continue
    if Searching:
        return A_bin
    return None

print(len(Program))
print(Program)
A_bin_options = [[]]
for j in range(len(Program)):
    new_A_bin_options = []
    for A_bin_prev in A_bin_options:
        new_options = []
        for i in range(0,8):
            to_add = int_to_bin_list(i)
            for _ in range(3-len(to_add)):
                to_add.append(0)
            new_options.append(to_add + A_bin_prev)
        print(new_options)
        for A_bin in new_options:
            res = check_options(A_bin, Program[(15-j):])
            print(res)
            if res is not None:
                print(f"Thing addded: {A_bin}")
                new_A_bin_options.append(A_bin)
    A_bin_options = new_A_bin_options


for A_bin in A_bin_options:
    print(bin_list_to_int(A_bin))


# submit(answer2, part="b", day=day, year=year)

