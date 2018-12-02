from aocd import get_data
import time

data = get_data(day=2, year=2018)
data = data.split('\n')


def part1():
    return None


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
