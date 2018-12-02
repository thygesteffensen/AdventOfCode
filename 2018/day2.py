import time
from aocd import get_data

data = get_data(day=2, year=2018)
data = data.split('\n')


def part1():
    sum_2 = 0
    sum_3 = 0

    for line in data:
        letters = set()
        letters_count = {}
        for char in line:
            if char in letters:
                if char in letters_count:
                    letters_count[char] += 1
                else:
                    letters_count[char] = 2

            letters.add(char)

        if 2 in letters_count.values():
            sum_2 += 1
        if 3 in letters_count.values():
            sum_3 += 1

    return sum_2 * sum_3


def part2():
    for i in data:
        for j in data:
            diffs = 0
            for idx, ch in enumerate(i):
                if ch != j[idx]:
                    diffs += 1
            if diffs == 1:
                ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
                print("Part Two:", ''.join(ans))


# Main part
start_time = time.time()
checksum = part1()
print("Part one. The checksum is: {} and it took {} seconds to calculate it!".
      format(checksum, round((time.time() - start_time), 4)))

start_time = time.time()
checksum = part2()
print("Part two. The checksum is: {} and it took {} seconds to calculate it!".
      format(checksum, round((time.time() - start_time), 4)))
