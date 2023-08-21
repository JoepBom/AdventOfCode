import math
class Monkey():
    items: list
    operation: callable
    test: int
    if_false: int
    if_true: int
    inspected_items = 0

    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test=test
        self.if_true=if_true
        self.if_false=if_false
        pass

    def pass_items(self):
        passing_list = []
        self.inspected_items+=len(self.items)
        for item in self.items:
            if item%self.test==0:
                passing_list.append([item, self.if_true])
            else:
                passing_list.append([item, self.if_false])
        self.items=[]
        return passing_list

monkeys=[]

modulo = 17*2*5*3*7*13*19*11

def func0(self):
    self.items=[math.floor(item*7%modulo) for item in self.items]
    return
monkeys.append(Monkey([54, 61, 97, 63, 74], func0, 17, 5, 3))
def func0(self):
    self.items=[math.floor(( item+8 )%modulo) for item in self.items]
    return 
monkeys.append(Monkey([61, 70, 97, 64, 99, 83, 52, 87], func0, 2, 7, 6))
def func0(self):
    self.items=[math.floor(( item * 13 ) %modulo) for item in self.items]
    return 
monkeys.append(Monkey([60, 67, 80, 65], func0, 5, 1, 6))
def func0(self):
    self.items=[math.floor(( item + 7) %modulo) for item in self.items]
    return 
monkeys.append(Monkey([61, 70, 76, 69, 82, 56], func0, 3, 5, 2))
def func0(self):
    self.items=[math.floor(( item  + 2) %modulo) for item in self.items]
    return 
monkeys.append(Monkey([79, 98], func0, 7, 0, 3))
def func0(self):
    self.items=[math.floor(( item + 1) %modulo) for item in self.items]
    return  
monkeys.append(Monkey([72, 79, 55], func0, 13, 2, 1))
def func0(self):
    self.items=[math.floor(( item + 4 ) %modulo) for item in self.items]
    return 
monkeys.append(Monkey([63], func0, 19, 7, 4))
def func0(self):
    self.items=[math.floor(( item  * item) %modulo) for item in self.items]
    return
monkeys.append(Monkey([72, 51, 93, 63, 80, 86, 81], func0, 11, 0, 4))


# def func0(self):
#     self.items=[math.floor(item* 19 %modulo) for item in self.items]
#     return
# monkeys.append(Monkey([79, 98], func0, 23, 2, 3))
# def func0(self):
#     self.items=[math.floor(( item+ 6 ) %modulo) for item in self.items]
#     return 
# monkeys.append(Monkey([54, 65, 75, 74], func0, 19, 2, 0))
# def func0(self):
#     self.items=[math.floor(( item * item ) %modulo) for item in self.items]
#     return 
# monkeys.append(Monkey([79, 60, 97], func0, 13, 1, 3))
# def func0(self):
#     self.items=[math.floor(( item + 3) %modulo) for item in self.items]
#     return 
# monkeys.append(Monkey([74], func0, 17, 0, 1))


for i in range(10000):
    print(f"round {i+1}")
    for l, m in enumerate(monkeys):
        # print(f"turn of monkey {l}")
        m.operation(m)
        for k in m.pass_items():
            monkeys[k[1]].items.append(k[0])
        # for j,m in enumerate(monkeys):
        #     print(f"monkey {j} has items: {m.items}")


monkey_activities = sorted([m.inspected_items for m in monkeys])
print(monkey_activities)
print(monkey_activities[-1]*monkey_activities[-2])

