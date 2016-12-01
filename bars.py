import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return json.load(data_file)


def get_biggest_bar(bars):
    maximum_seats = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return maximum_seats['Cells']['Name']


def get_smallest_bar(bars):
    minimun_seats = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return minimun_seats['Cells']['Name']


def get_closest_bar(bars, longitude, latitude):
    closest_bar = min(bars, key=lambda x: (x['Cells']['geoData']['coordinates'][0]-longitude) ** 2 + (x['Cells']['geoData']['coordinates'][1]-latitude) ** 2)
    return closest_bar['Cells']['Name']

if __name__ == '__main__':
    all_bars_information_json = load_data(input('Введите путь до файла: '))
    print('Самый большой бар: {}' .format(get_biggest_bar(all_bars_information_json)))
    print('Самый маленький бар: {}' .format(get_smallest_bar(all_bars_information_json)))
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    print('Самый близкий бар: {}' .format(get_closest_bar(all_bars_information_json, longitude, latitude)))
