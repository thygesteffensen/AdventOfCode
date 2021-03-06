import collections
import datetime

from aocd import get_data
import time
import datetime
import collections

# data = get_data(day=4, year=2018)

data = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''

data = data.split('\n')


def part1():
    time_list = sorted(data)
    guard_sleep_time = collections.defaultdict(int)
    guards = collections.defaultdict(list)

    current_guard = None
    fall_asleep_time = None

    for time_input in time_list:

        if get_guard_id(time_input)[0]:
            current_guard = get_guard_id(time_input)[1]
            continue

        if fall_asleep_time is None:
            fall_asleep_time = get_time(time_input)
            continue

        wake_up_time = get_time(time_input).minute
        delta_time = wake_up_time - fall_asleep_time.minute
        guard_sleep_time[current_guard] += delta_time
        guards[current_guard].append((fall_asleep_time.minute, wake_up_time))
        fall_asleep_time = None

    (guard, time) = max(guard_sleep_time.items(), key=lambda i: i[1])
    minute_list = guards[guard]
    minute_list_add = collections.defaultdict(int)

    for minute in minute_list:
        for clock_minute in range(minute[0], minute[1]):
            value = int(minute_list_add[clock_minute])
            minute_list_add[clock_minute] = value + 1

    return int(int(max(minute_list_add, key=minute_list_add.get))) * int(guard)


def get_time(data_set):
    data_set = data_set.split(' ')
    return datetime.datetime.strptime(data_set[1][:-1], '%H:%M').time()


def get_guard_id(data_set):
    if '#' not in data_set:
        return False, 0
    data_set = data_set.split(' ')
    return True, data_set[3][1:]

    # dict = Date, id, total sleep time
    guard_list = []
    for data_set in data:
        date, guard_id, action = parse_data(data_set)
        guard_list.append({'date': date, 'guard_id': guard_id, 'action': action})

    # Sort data according to date
    guard_list = sorted(guard_list, key=lambda k: k['date'])
    for guard in guard_list:
        print(guard)

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
            fall_time = guard.get('date').minute
            wake_time = None
            continue

        if wake_time is None:
            wake_time = guard.get('date').minute

            delta_time = wake_time - fall_time -1
            guard_list_sleep[current_guard_id] += delta_time

            wake_time = None
            fall_time = None

    (guard, time) = max(guard_list_sleep.items(), key=lambda i: i[1])

    return 'guard: {} and sleep: {}. Result: {}'.format(guard, time, int(time)*int(guard))



def part2():
    time_list = sorted(data)
    guards = collections.defaultdict(list)
    minute_list_add = collections.defaultdict(int)

    current_guard = None
    fall_asleep_time = None

    for time_input in time_list:

        if get_guard_id(time_input)[0]:
            current_guard = get_guard_id(time_input)[1]
            continue

        if fall_asleep_time is None:
            fall_asleep_time = get_time(time_input)
            continue

        wake_up_time = get_time(time_input).minute

        for clock_minute in range(fall_asleep_time.minute, wake_up_time):
            value = int(minute_list_add[clock_minute])
            guards[current_guard][clock_minute] = value + 1

        fall_asleep_time = None

    # Find all guards max minute, then find this max
    guard_added_list = collections.defaultdict(list)
    for i, guard in guards:
        (minute, occurrence) = max(guard.items(), key=lambda i: i[1])
        guard_added_list[i] = (minute, occurrence)



    # (guard, time) = max(guard_sleep_time.items(), key=lambda i: i[1])
    # minute_list = guards[guard]
    # minute_list_add = collections.defaultdict(int)


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
