

def check_solution(number):
    string = str(number)
    Condition1 = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and (i == 0 or string[i - 1] != string[i]) and (i == len(string) - 2 or string[i + 2] != string[i + 1]):
            Condition1 = True
    if not Condition1:
        return False
    Condition2 = True
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            Condition2 = False
    if not Condition2:
        return False
    return True

count = 0
for i in range(206938, 679128):
    if check_solution(i):
        print(i)
        count += 1

print(count)