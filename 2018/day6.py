from collections import defaultdict

from aocd import get_data
import time

data = get_data(day=2, year=2018)

data = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''

data = data.split('\n')


def part1():
    # Added all coordinates to a dict
    coordinates = set()
    max_x = max_y = 0
    for coordinate in data:
        x, y = map(int, get_coordinate_set(coordinate))
        coordinates.add((x, y))

    infinite_coordinates = set()
    size = defaultdict(int)
    # Go through every point on the every coordinate
    # Mark it with the id, of the closets point.
    # If two points are equally close, mark it -1
    # Create list of infinite coordinates, these
    # should not be accounted for.
    # Now find the value, with most occurrences and
    # return the number of occurrences.

    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            min_dist = []
            for i, (x1,y1) in coordinates:
                distance = abs(x1 - x) + abs(y1 - y)
                min_dist.append((distance, i))

            min_dist = sorted(min_dist)

            if len(min_dist) == 1 or min_dist[0][0] != min_dist[1][0]:
                size[min_dist[0][1]] += 1

                if x == 0 or y == 0 or x == max_x or y == max_y:
                    infinite_coordinates.add((x, y))

    return None


def get_coordinate_set(coordiante):
    coordiante = coordiante.split()
    return coordiante[0][:-1], coordiante[1]


def part2():
    return None


# Main part
start_time_1 = time.time()
result_1 = part1()
start_time_2 = time.time()
result_2 = part2()
print("Part one result: {}. \t Duration: {} sec."
      "\nPart two result: {}. \t Duration: {} sec.".
      format(result_1, round((start_time_2 - start_time_1), 4), result_2, round((time.time()) - start_time_2, 4)))
