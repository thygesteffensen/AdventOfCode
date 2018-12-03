from aocd import get_data
import time
import numpy

data = get_data(day=3, year=2018)
data = data.split('\n')


def part1():
    size = 1000
    matrix = numpy.zeros((size, size))
    for data_set in data:
        id, x, y, width, height = parse_input(data_set)
        matrix[x:x + width, y:y + height] += 1
    return numpy.size(numpy.where(matrix >= 2)[0])


def part2():
    size = 1000
    matrix = numpy.zeros((size, size))
    for data_set in data:
        id, x, y, width, height = parse_input(data_set)
        matrix[x:x + width, y:y + height] += 1
    for data_set in data:
        id, x, y, width, height = parse_input(data_set)
        if numpy.all(matrix[x:x + width, y:y + height] == 1):
            return id


def parse_input(data_set):
    id, _, coordinates, size = data_set.split(' ')
    x, y = map(int, coordinates[:-1].split(','))
    width, height = map(int, size.split('x'))
    return id, x, y, width, height


# Main part
start_time_1 = time.time()
result_1 = part1()
start_time_2 = time.time()
result_2 = part2()
print("Part one result: {}. \t Duration: {} sec."
      "\nPart two result: {}. \t Duration: {} sec.".
      format(result_1, round((start_time_2 - start_time_1), 4), result_2, round((time.time()) - start_time_2, 4)))
