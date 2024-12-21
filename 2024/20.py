from aocd.models import Puzzle
from aocd import submit

def get_input(year=2024, day=1, example=False):
    puzzle = Puzzle(year,day)
    if example:
        return puzzle.examples[0].input_data
    return puzzle.input_data

def parse_input(input):
    walls = set()
    for x, line in enumerate(input.splitlines()):
        for y, char in enumerate(line):
            if char == "#":
                walls.add((x,y))
            if char == "S":
                start = (x,y)
            if char == "E":
                end = (x,y)
    return walls, start, end

def get_distances(walls, start, end):
    visited = set()
    distances = dict()
    distances[start] = 0
    current_node = start
    current_dist = 0
    while True:
        for dir in ((0,1), (1,0), (0,-1), (-1,0)):
            new_node = (current_node[0] + dir[0], current_node[1] + dir[1])
            if new_node in walls or new_node in visited:
                continue
            break
        distances[new_node] = current_dist + 1
        visited.add(current_node)
        current_node = new_node
        current_dist += 1
        if new_node == end:
            break
    return distances


def get_cheats(distances, max_cheat_length):
    land_options_dydx = set()
    for dir_x in (-1,1):
        for dir_y in (-1,1):
            for i in range(max_cheat_length+1):
                for j in range(max_cheat_length+1-i):
                    land_options_dydx.add((i*dir_x, j*dir_y))

    cheat_dists = dict()
    for S in distances:
        for dir2 in land_options_dydx:
            land = (S[0] + dir2[0], S[1] + dir2[1])
            if land not in distances:
                continue
            dist_cheated = distances[land]-distances[S] - abs(dir2[0]) - abs(dir2[1])
            if dist_cheated > 0:
                if dist_cheated in cheat_dists:
                    cheat_dists[dist_cheated] += 1
                else:
                    cheat_dists[dist_cheated] = 1
    return cheat_dists

if __name__ == "__main__":
    year = 2024
    day = 20

    input = get_input(day=20, example=False)
    walls, start, end = parse_input(input)
    distances = get_distances(walls, start, end)

    cheat_dists = get_cheats(distances, 2)
    answer1 = sum(amount for dist, amount in cheat_dists.items() if dist >= 100)
    submit(answer1, part="a", day=day, year=year)

    cheat_dists = get_cheats(distances, 20)
    answer2 = sum(amount for dist, amount in cheat_dists.items() if dist >= 100)
    submit(answer2, part="b", day=day, year=year)

