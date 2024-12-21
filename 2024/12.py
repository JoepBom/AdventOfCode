from aocd.models import Puzzle
from aocd import submit

year=2024
day=12
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()

visited = set()
areas = dict()
answer1=0
answer2=0
for x1, line in enumerate(input):
    for y1, char in enumerate(line):
        if char not in areas:
            areas[char] = []
        if (x1,y1) in visited:
            continue
        areas[char].append({(x1,y1)})
        fences_cnt = 0
        fences = {"N":set(), "S":set(), "E":set(), "W":set()}
        new_area_added = True
        while new_area_added:
            new_area_added = False
            to_add = set()
            for x,y in areas[char][-1]:
                if (x,y) in visited:
                    continue
                visited.add((x,y))
                for dx in (-1,0,1):
                    for dy in (-1,0,1):
                        if (dx != 0 and dy != 0) or dx == dy == 0:
                            continue
                        if x+dx < 0 or y+dy < 0 or x+dx >= len(input) or y+dy >= len(input[0]) or input[x+dx][y+dy] != char:
                            if dx == 0:
                                if dy == -1:
                                    fences["W"].add((y,x))
                                else:
                                    fences["E"].add((y,x))
                            else:
                                if dx == -1:
                                    fences["N"].add((x,y))
                                else:
                                    fences["S"].add((x,y))
                            fences_cnt += 1
                            continue
                        if input[x+dx][y+dy] == char:
                            to_add.add((x+dx,y+dy))
                            new_area_added = True
            areas[char][-1]= areas[char][-1].union(to_add)

        answer1+=fences_cnt*len(areas[char][-1])
        side_count = 0

        for direction in fences:
            for dir1 in set(dir1 for dir1,_ in fences[direction]):
                prev_dir2 = None
                for dir2 in sorted(dir2 for tmp,dir2 in fences[direction] if tmp == dir1):
                    if prev_dir2 is None or dir2-prev_dir2 != 1:
                        side_count += 1
                    prev_dir2 = dir2
        answer2+=side_count*len(areas[char][-1])




print(list((key, len(val)) for key,val in areas.items()))

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)
