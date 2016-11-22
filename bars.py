import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return json.load(data_file)


def get_biggest_bar(data):
    seats_count_all_bars = [data[i]['Cells']['SeatsCount'] for i in range(len(data))]
    maximum_seats = max(seats_count_all_bars)
    for bar in data:
        if bar['Cells']['SeatsCount'] == maximum_seats:
            biggest_bar_name = bar['Cells']['Name']
            return biggest_bar_name


def get_smallest_bar(data):
    seats_count_all_bars = [data[i]['Cells']['SeatsCount'] for i in range(len(data))]
    minimun_seats = min(seats_count_all_bars)
    for bar in data:
        if bar['Cells']['SeatsCount'] == minimun_seats :
            smallest_bar_name = bar['Cells']['Name']
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
    print('Самый большой бар: {}' .format(get_biggest_bar(data)))
    print('Самый маленький бар: {}' .format(get_smallest_bar(data)))
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    print('Самый близкий бар: {}' .format(get_closest_bar(data, longitude, latitude)))