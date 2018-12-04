from aocd import get_data
import time
import datetime
import collections

data = get_data(day=4, year=2018)
data = data.split('\n')


def part1():
    # dict = Date, id, total sleep time
    guard_list = []
    for data_set in data:
        date, guard_id, action = parse_data(data_set)
        guard_list.append({'date': date, 'guard_id': guard_id, 'action': action})

    # Sort data according to date
    guard_list = sorted(guard_list, key=lambda k: k['date'])

    # Calculate the guard with most sleeping minutes
    current_guard_id = None
    fall_time = None
    wake_time = None

    guard_list_sleep = collections.defaultdict(int)

    for guard in guard_list:
        if guard.get('guard_id') is not None:
            current_guard_id = guard.get('guard_id')
            continue

        if fall_time is None:
            fall_time = guard.get('date').time()
            wake_time = None
            continue

        if wake_time is None:
            wake_time = guard.get('date').time()
            guard_list_sleep[current_guard_id] += wake_time-fall_time

            wake_time = None
            fall_time = None

    for guard in guard_list_sleep:
        print(guard)

    return None


def part2():
    return None


def parse_data(data_set):
    date, time, additional = data_set.split(' ', maxsplit=2)
    date = '{}_{}'.format(date[1:], time[:-1])
    date = datetime.datetime.strptime(date, "%Y-%m-%d_%H:%M")

    additional = additional.split(' ')
    if len(additional) > 2:
        guard_id = additional[1][1:]
        action = additional[2]
    else:
        guard_id = None
        action = additional[0]

    return date, guard_id, action


# Main part
start_time_1 = time.time()
result_1 = part1()
start_time_2 = time.time()
result_2 = part2()
print("Part one result: {}. \t Duration: {} sec."
      "\nPart two result: {}. \t Duration: {} sec.".
      format(result_1, round((start_time_2 - start_time_1), 4), result_2, round((time.time()) - start_time_2, 4)))
