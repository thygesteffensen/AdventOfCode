from aocd import get_data

data = get_data(day=1, year=2018)
data = data.split('\n')

sum = 0
for line in data:
    sum += int(line[1:])

print(sum)


data = get_data(day=1, year=2018)
data = data.split('\n')

sum_set = set()
sum = 0

bool = True
while bool:
    for line in data:
        sum += int(line)

        if sum in sum_set:
            print(sum)
            bool = False
            break
        else:
            sum_set.add(sum)
