def read_stats():
    with open("stats.txt", "r") as file:
        document = file.readlines()
    return document[0], document[1:]

def results_to_arr(elements):
    trimed_arr = []
    for el in elements:
        trimed_arr.append(el.strip().split(';'))
    return trimed_arr

def header_to_arr(elements):
    return elements.strip().split(';')

def data_by_years():
    header_names, results = read_stats()
    stats = header_to_arr(header_names)
    elements = results_to_arr(results)
    
    dict_by_years = {}
    for el in elements:
        year_fields = {}
        for i in range(1, len(stats)):
            year_fields[stats[i]] = el[i]
        dict_by_years[el[0]] = year_fields
    return stats, dict_by_years

def find_in_dict(years, input_stats):
    year_from, year_to = years.split('-')
    headers, data = data_by_years()
    
    stats = input_stats.split(',')
    if stats[0] == '':
        stats = headers[2:]

    average_dict = {}
    for stat in stats:
        average = 0
        counter = 0
        for key, value in data.items():
            key_from, key_to = key.split('-')
            if (year_from <= key_from and year_to >= key_to):
                counter += 1
                average += float(value[stat])
                average_dict[stat] = round(average / counter, 2)
    if len(average_dict) == 0: return 'No data found'
    return average_dict
    

years = input('Please enter year in format YYYY-YY\n')
print('Please enter stats from following list and separate individual stats with ",".\n')
input_stats = input('GP, GS, MPG, FG, 3P, FT, RPG, APG, SPG, BPG, PPG\n').upper()

print(find_in_dict(years, input_stats))