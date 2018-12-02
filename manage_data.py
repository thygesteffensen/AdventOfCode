from aocd import get_data
import time
import os

os.environ["AOC_SESSION"] = \
    "53616c7465645f5f2ffc2f3199d9f48731bdd78867a87322ffe86cbe91720cc4c87f92d27c22fa72d1ac91319850fa5b"

current_date = int(time.strftime('%d'))
current_year = time.strftime('%Y')
file_name = 'data_day_{}.txt'.format(current_date)

try:
    os.mkdir('data_sets/{}'.format(current_year))
except FileExistsError as e:
    print("The directory already exists!")

os.chdir('data_sets/{}'.format(current_year))


def get_day_data():
    if check_if_already_exists():
        return read_data_from_file()
    else:
        get_data_from_aoc()

    return read_data_from_file()


def get_data_from_aoc():
    data = get_data(day=current_date, year=current_year)
    data = data.split('\n')

    file = open(file_name, 'w+')

    for line in data:
        file.write(line + '\n')

    file.close()


def check_if_already_exists():
    if os.path.exists(file_name):
        return True
    return False


def read_data_from_file():
    return [line.rstrip('\n') for line in open(file_name)]
