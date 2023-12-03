from pprint import pprint
file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\15\input.txt", "r")
input = []
sensors = []
closest_beacons = []
for line in file.readlines():
    i=line.strip().split(" ")
    sensors.append([int(i[2][2:-1]), int(i[3][2:-1])])
    closest_beacons.append([int(i[8][2:-1]), int(i[9][2:])])
dist = []
blocked_spots=set()
for i, sensor in enumerate(sensors):
    dist.append(abs(sensor[0]- closest_beacons[i][0])+ abs(sensor[1]-closest_beacons[i][1]))
max = 4000000
corner_coordinates = (0,max,0,max)
def check_area(corner_coordinates):
    # print(corner_coordinates)
    for i, sens in enumerate(sensors):
        contained=True
        for x in [0,1]:
            for y in [2,3]:
                if not abs(corner_coordinates[x]-sens[0])+abs(corner_coordinates[y]-sens[1])<= dist[i]:
                    contained=False
                    break
        if contained:
            # print("contained", i)
            return 0
    if corner_coordinates[1]-corner_coordinates[0] == 0 and corner_coordinates[3]-corner_coordinates[2] == 0:
        return (corner_coordinates[0], corner_coordinates[2])
    if corner_coordinates[1]-corner_coordinates[0] <= 1 and corner_coordinates[3]-corner_coordinates[2] <= 1:
        res = check_area([corner_coordinates[0], corner_coordinates[0], corner_coordinates[2], corner_coordinates[2]])
        if res != 0:
            return res
        res = check_area([corner_coordinates[0], corner_coordinates[0], corner_coordinates[3], corner_coordinates[3]])
        if res != 0:
            return res
        res = check_area([corner_coordinates[1], corner_coordinates[1], corner_coordinates[2], corner_coordinates[2]])
        if res != 0:
            return res
        res = check_area([corner_coordinates[1], corner_coordinates[1], corner_coordinates[3], corner_coordinates[3]])
        if res != 0:
            return res
        return 0
    middle_point = [corner_coordinates[0]+(corner_coordinates[1]-corner_coordinates[0])//2, corner_coordinates[2]+(corner_coordinates[3]-corner_coordinates[2])//2]
    new_corners = [corner_coordinates[0], middle_point[0], corner_coordinates[2], middle_point[1]]
    res = check_area(new_corners)
    if res != 0:
        return res
    new_corners = [middle_point[0], corner_coordinates[1], corner_coordinates[2], middle_point[1]]
    res = check_area(new_corners)
    if res != 0:
        return res
    new_corners = [corner_coordinates[0], middle_point[0], middle_point[1], corner_coordinates[3]]
    res = check_area(new_corners)
    if res != 0:
        return res
    new_corners = [middle_point[0], corner_coordinates[1], middle_point[1], corner_coordinates[3]]
    res = check_area(new_corners)
    if res != 0:
        return res
    return 0

res = check_area(corner_coordinates)
print(4000000*res[0]+res[1])







