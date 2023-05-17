﻿"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
from pprint import pprint


student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '380987771221',
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
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
student.setdefault("Віктор Нагреба", {'Пошта': 'viktor@gmail.com','Вік': 25,'Номер телефону': '+380986623521','Середній бал': 65})
pprint(student)

student_list = {'Юліанна Пижик': {'Група': 101,'Номер телефону': '+380973489956', 'Середній бал': 34}, 'Ігор Максимюк': {'Група': 106, 'Номер телефону': '', 'Середній бал': 182}, 'Орест Винницький': {'Група': 101,'Номер телефону': '+380974569811', 'Середній бал': 112}, 'Ілона Кук': {'Група': 19,'Номер телефону': '+380686669801', 'Середній бал': 99}, 'Олена Куч': {'Група': 19,'Номер телефону': '+380686669801', 'Середній бал': 65}, 'Кристіан Данелюк': {'Група': 42, 'Номер телефону': '', 'Середній бал': 106}}
suma_balls = 0
number_students = 0
for key in student_list:
    if student_list[key]['Середній бал'] > 90:
        print(key, student_list[key])
    suma_balls = suma_balls + student_list[key]['Середній бал']
    if student_list[key]['Номер телефону'] == '':
        parents_number = input('Введіть номер телефону батьків :')
        student_list[key]['Номер телефону'] = parents_number
    number_students = number_students + 1
pprint(student_list)
print('Середній бал по групі: ', suma_balls/number_students)


# ваш код нижче
