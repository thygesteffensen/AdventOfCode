from aocd import get_data
import time
import numpy

data = get_data(day=3, year=2018)
data = data.split('\n')


def part1():
    number_of_overlaps = 0
    rows = 1100
    columns = 1100
    matrix = numpy.zeros((columns, rows))
    matrix[0, 0] = 1
    for data_set in data:
        dict_coor = get_coordinates(data_set)
        dict_size = get_size(data_set)

        # already_counted_for = False
        for x in range(int(dict_size[0])):
            for y in range(int(dict_size[1])):
                # if matrix[int(dict_coor[0]) + int(x), int(dict_coor[1]) + int(y)] > 1.0 and not already_counted_for:
                if matrix[int(dict_coor[0]) + int(x) + 1, int(dict_coor[1]) + int(y) + 1] > 1.0:
                    # already_counted_for = True
                    number_of_overlaps += 1
                matrix[int(dict_coor[0]) + int(x) + 1, int(dict_coor[1]) + int(y) + 1] += 1

    return number_of_overlaps


def get_coordinates(data_set):
    data_set = data_set.split('@')[1]
    data_set = data_set.split(':')[0]
    data_set = data_set.lstrip()
    data_set = data_set.split(',')
    return data_set


def get_size(data_set):
    data_set = data_set.split(':')[1]
    data_set = data_set.lstrip()
    data_set = data_set.split('x')
    return data_set


def part2():
    return None

# Real result 1 : 120408
# Main part
start_time_1 = time.time()
result_1 = part1()
start_time_2 = time.time()
result_2 = part2()
print("Part one result: {}. \t Duration: {} sec."
      "\nPart two result: {}. \t Duration: {} sec.".
      format(result_1, round((start_time_2 - start_time_1), 4), result_2, round((time.time()) - start_time_2, 4)))
