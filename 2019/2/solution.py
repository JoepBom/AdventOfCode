
filepath="2019/2/input.txt"

with open(filepath) as file:
    input = file.readlines()[0].split(",")

input = [int(i) for i in input]
input_copy = input.copy()
for j in range(100):
    for k in range(100):
        input = input_copy.copy()
        input[1] = j
        input[2] = k
        i=0
        while input[4*i]!=99:
            if input[4*i] == 1:
                input[input[4*i+3]] = input[input[4*i+1]] + input[input[4*i+2]]
            if input[4*i] == 2:
                input[input[4*i+3]] = input[input[4*i+1]] * input[input[4*i+2]]
            i+=1
        if input[0] == 19690720:
            print(100*j+k)
            break

