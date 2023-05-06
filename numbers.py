user_name = input('Please, enter your name >>> ').title().strip(' 1234567890')
user_surname = input('Please, enter your surname >>> ').upper().strip(' 1234567890')
letters_number = str(len(user_name))
greeting = 'Привіт, ' + user_name + ' ' + user_surname
serlock_adress = greeting.replace('Привіт, ', 'Здоров, ')
result = serlock_adress + ', а ти знав, що твоє імя складється з ' + letters_number + ' літер'
print(f"{result}?")
