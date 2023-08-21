from pprint import pprint
file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\15\input.txt", "r")
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
# corner_coordinates (x_0,x_1,y_0,y_1)
def check_area(corner_coordinates, level):
    for i, sens in enumerate(sensors):
        contained=True
        for x in [0,1]:
            for y in [0,1]:
                if not abs(corner_coordinates[x]-sens[0])+abs(corner_coordinates[y]-sens[1])<= dist[i]:
                    contained=False
                    break
        if contained:
            return 0
        middle_point = [corner_coordinates[0]+(corner_coordinates[1]-corner_coordinates[0])//2, corner_coordinates[2]+(corner_coordinates[3]-corner_coordinates[2])//2]
        return check_area()


