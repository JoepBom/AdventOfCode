
filepath="2019/1/input.txt"

with open(filepath) as file:
    input = file.readlines()

fuel_list = [[int(i)//3-2 for i in input]]
print(sum([sum(i) for i in fuel_list]))
while len(fuel_list[-1]) > 0:
    fuel_list.append([i//3-2 for i in fuel_list[-1] if i//3-2 > 0])

print(sum([sum(i) for i in fuel_list]))