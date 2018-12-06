from aocd import get_data
import time

data = get_data(day=5, year=2018)


def part1():
    line_current = data
    line_old = None
    while line_old != line_current:
        line_old = line_current

        for i in range(26):
            line_current = line_current.replace(chr(65 + i) + chr(97 + i), "")
            line_current = line_current.replace(chr(97 + i) + chr(65 + i), "")

    return len(line_current)


def part2():
    shortest = len(data)

    for i in range(26):
        line_current = data
        line_current = line_current.replace(chr(65 + i), "")
        line_current = line_current.replace(chr(97 + i), "")
        line_old = None

        while line_old != line_current:
            line_old = line_current

            for j in range(26):
                line_current = line_current.replace(chr(65 + j) + chr(97 + j), "")
                line_current = line_current.replace(chr(97 + j) + chr(65 + j), "")

            if shortest > len(line_current):
                shortest = len(line_current)

    return shortest


# Main part
start_time_1 = time.time()
result_1 = part1()
start_time_2 = time.time()
result_2 = part2()
print("Part one result: {}. \t Duration: {} sec."
      "\nPart two result: {}. \t Duration: {} sec.".
      format(result_1, round((start_time_2 - start_time_1), 4), result_2, round((time.time()) - start_time_2, 4)))
