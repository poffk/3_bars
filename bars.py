import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return json.load(data_file)


def get_biggest_bar(data):
    number_of_bars = len(data)
    maximum_seats = data[0]['Cells']['SeatsCount']
    while number_of_bars != 0:
        number_of_bars = number_of_bars - 1
        if data[number_of_bars]['Cells']['SeatsCount'] > maximum_seats:
            maximum_seats = data[number_of_bars]['Cells']['SeatsCount']
            biggest_bar_name = data[number_of_bars]['Cells']['Name']
    return biggest_bar_name


def get_smallest_bar(data):
    number_of_bars = len(data)
    minimum_seats = data[0]['Cells']['SeatsCount']
    while number_of_bars != 0:
        number_of_bars = number_of_bars - 1
        if data[number_of_bars]['Cells']['SeatsCount'] < minimum_seats:
            minimum_seats = data[number_of_bars]['Cells']['SeatsCount']
            smallest_bar_name = data[number_of_bars]['Cells']['Name']
    return smallest_bar_name


def get_closest_bar(data, longitude, latitude):
    coord = data[0]['Cells']['geoData']['coordinates']
    minimum_range = (coord[0]-longitude) ** 2 + (coord[1]-latitude) ** 2
    number_bars = len(data)
    for number_of_bar in range(number_bars):
        coord = data[number_of_bar]['Cells']['geoData']['coordinates']
        distance = (coord[0]-longitude) ** 2 + (coord[1]-latitude) ** 2
        if distance < minimum_range:
            minimum_range = distance
            closest_bar_name = data[number_of_bar]['Cells']['Name']
    return closest_bar_name


if __name__ == '__main__':
    data = (load_data(input('Введите путь до файла: ')))
    print('Самый большой бар: ' + get_biggest_bar(data))
    print('Самый маленький бар: ' + get_smallest_bar(data))
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    print('Самый близкий бар: ' + get_closest_bar(data, longitude, latitude))