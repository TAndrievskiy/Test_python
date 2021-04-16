"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

from pprint import pprint


def main():
    data = {
        "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
        }
    get_country(data)
    grouping_data(data)


def get_country(data):
    input_city = input("Enter the city:")
    for country, city in data.items():
        if input_city in city:
            print(f"Country: {country}")
            return country
        else:
            print("Wrong city, try again!")
            return get_country(data)


def grouping_data(data):
    country_list = list(data.keys())
    countries = dict.fromkeys(["country"], country_list)
    new_data = countries | capitals_and_cities(data)
    pprint(new_data)


def capitals_and_cities(data):
    city_list = list(data.values())
    capitals_list = list()
    cities_list = list()
    capital = ""
    city = ""
    for cities in city_list:
        for _ in cities:
            capital = cities[0]
            city = cities[1:]
        cities_list.append(city)
        capitals_list.append(capital)
    cities = dict.fromkeys(["cities"], cities_list)
    capitals = dict.fromkeys(["capitals"], capitals_list)
    return capitals | cities


if __name__ == "__main__":
    main()
