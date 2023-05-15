##my_text = 'I love\npython'
##print(id(my_text))
##my_text += ' very \t\t\t\t much'
##print(id(my_text))
##
##some_new = my_text.split('v')
##print(some_new)
##print(type(some_new))
#from typing import Any
#
##new_list = [1, 5, 3.3, 666, 9999, -6]
##new_list_2 = [5555555]
##new_list_3 = list()
##
##length_list = len(new_list)
##
##new_list_2.append(100)
##new_list_2.append(654)
##print(new_list_2)
##pass
#
##new_list.append(1_000_000)
#
##print(id(new_list))
##print(new_list)
##new_list.sort()
##print(new_list)
##
##print(new_list[0])
##print(new_list[5])
##print(new_list[15])
##
##print(range(1,32))
#
##new_list_of_week_temperature.clear()
##new_list_of_week_temperature[]
## temp = flout(input(f'day {day}: enter '))
## for day in range(1, 32)
##     print(day)
##print(bool(new_list))
##print(bool(new_list_2))
##
##if new_list:
##    new_variable = 6666666
##    print(new_variable)
##else:
##    new_variable = 0
##
##print(new_variable)
##pass
#
##ukraine_cities = ['Lviv', 'Odesa', 'Zapori']
##city_list = []
##expenses = []
##some_trash_list = ['Lviv', 'Odesa', 'Dnipro', 'Petrovych 068567856']
##
##ukraine_cities.extend(some_trash_list)
##ukraine_cities.sort()
##print(ukraine_cities)
###value: str | int | float | Any
###for value in some_trash_list:
###    #if type(value) == str:
###    if isinstance(value, str) and value in ukraine_cities:
###        city_list.append(value)
###
###    #if type(value) == int or type(value) == float:
###    if isinstance(value, (int, float)):
###        expenses.append(value)
###
###print(city_list)
###print(expenses)
##
##print('f' in ukraine_cities)
##
##person['age']=
#
#set1 = set()
#print(set1)
#
#set2 = {5, 6, 6, 6, 'qq', 'k', 5.5, 7., True}
##print(set2)
##print(len(set2))
#
#
#
##unique_letters = set('London l')
##print(unique_cities)
#
##letters = list(unique_letters)
##print(letters)
#
## add element
#cities = ['Київ', 'London', 'lviv']
#unique_cities = set(cities)
#print(unique_cities)
#...
#unique_cities.add('Paris')
#unique_cities.add('Paris')
#print(unique_cities)
#unique_cities.update('asdyujk')
#print(unique_cities)
#print('a' in unique_cities)
#print(unique_cities)
##data = unique_cities.pop()
##print(data, unique_cities)
#unique_cities.discard('a')
#print(unique_cities)
#
#new_set_common = set1.intersection(set2)
#print(new_set_common)
#
#new_set_common_3_10_and_high = set1 & set2
#print(new_set_common_3_10_and_high)
#print(new_set_common == new_set_common_3_10_and_high)
#
#new_set_common = set1.intersection(set2)
#print(new_set_common)
#new_set_common_3_10_and_high = set1 & set2
#print(new_set_common_3_10_and_high)
#print(new_set_common == new_set_common_3_10_and_high)
#
#words = input('enter your text')
#print(words)

word = {'Lviv', 'Kyiv', 'Odesa'}
word_add = word.update('Lviv', London)
print(word_add)

