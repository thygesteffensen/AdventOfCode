import collections, dateutil
from aocd import get_data

inp = get_data(day=4, year=2018)
# inp = data.split('\n')

guards = collections.defaultdict(list)
times = collections.defaultdict(int)

for line in sorted(inp(4).splitlines()):
    time, action = line.split('] ')

    time = dateutil.parser.parse(time[1:])

    if action.startswith('Guard'):
        guard = int(action.split()[1][1:])
    elif action == 'falls asleep':
        start = time
    elif action == 'wakes up':
        end = time
        guards[guard].append((start.minute, end.minute))
        times[guard] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60)], key=lambda i: i[1])

print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('part 2:', guard * minute)