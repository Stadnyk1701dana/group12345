#from decimal import Decimal


list = [1, 8.49, 0.5, 7000, 50.9, 3, 29, 66.99]
new_list = []
for list_element in list:
    new_element = str(list_element*2)
    new_list.append(new_element)
print(new_list )

surnames = input('ВВедіть список прізвищa: ')
list_surname = surnames.split()
list_surname.sort()
for surname_element in list_surname:
    surname_title = surname_element.title()
    print(surname_title)

user_string = input('Введіть стрічку з символами:')
new_string = ''
for string_element in user_string:
    if string_element.isupper():
        new_string = new_string + string_element
print(new_string)

for day in range(0,7):
    temp_c = float(input('Введіть температуру (по шкалі Цельсія С): '))
    temp_f = ((temp_c + 40) * 1.8)-40
    #print(temp_f.quantize(Decimal('0.1')))
    print(temp_f)


