import json
from typing import TextIO

# {
#     '2003-04': {
#         'Team': 'Cleveland'
#         'GP': 80,
#         'GS': 80,
#         ...
#         'PPG: 20.9
#     },
#     ...
#     '2021-2022': {
#         'Team': 'Lakers'
#         'GP': 56,
#         'GS': 56,
#         ...
#         'PPG': 30.3
#     }
# }


def open_stats(file: str) -> tuple[str, list[str]]:
    with open(file) as file_handler:
        stats = file_handler.readlines()
    return stats[0], stats[1:]

def stat_to_dict(stat_keys: list, stats: list) -> dict:
    stat_dict = {}
    for key, value in zip(stat_keys, stats):
        stat_dict[key] = value

    return stat_dict

def generate_main_dict(stat_keys: str, stats: list[str]) -> dict:
    keys_list = stat_keys.strip().split(';')
    main_dict = {}
    for stat in stats:
        stat_list = stat.strip().split(';')
        main_dict[stat_list[0]] = stat_to_dict(keys_list[1:], stat_list[1:])
    return main_dict


stats = 'stats.txt'

stat_keys, results = open_stats(stats)
main_stats = generate_main_dict(stat_keys, results)

year = input('Please enter year in format YYYY-YY')
stats = input('Please enter stats')

# print(main_stats[year])

for stat in stats.split(','):
    print(f'{stat}: {main_stats.get(year).get(stat)}')

