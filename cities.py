from pprint import pprint


past_cities = input('Введіть міста, які ви відвідали за останні 10 років >>>>')
future_cities = input('Введіть міста, які ви хочете відвідати за наступні 10 років >>>>')
list_past_cities = past_cities.split()
list_future_cities = future_cities.split()
past_cities_1 = set(list_past_cities)
future_cities_1 = set(list_future_cities)
favourite_cities = past_cities_1.intersection(future_cities_1)
print('Вам дуже сподобалось в містах:', favourite_cities)
favourite_cities_1 = len(favourite_cities)
if favourite_cities_1 == 0:
    print('Ви відкриті до подорожей у нові міста!')

print(past_cities_1)
print(future_cities_1)





students = {
  'Іван Петров': {
    'Пошта': 'Ivan@gmail.com',
    'Вік': 14,
    'Номер телефону': '+380987771221',
    'Середній бал': 95.8
  },
  'Женя Курич': {
    'Пошта': 'Geka@gmail.com',
    'Вік': 16,
    'Номер телефону': None,
    'Середній бал': 64.5
  },
  'Маша Кера': {
    'Пошта': 'Masha@gmail.com',
    'Вік': 18,
    'Ном'
    'ер телефону': '+380986671221',
    'Середній бал': 80
  },
}
students_number = set(students)
print('Кількість елементів словника', len(students_number))
students['Женя Курич'] = {
    'Пошта': 'Geka@gmail.com',
    'Вік': 25,
    'Номер телефону': None,
    'Середній бал': 64.5
  }
pprint(students)

