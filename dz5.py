User_name =input ('Please, enter your name >>> ').title().strip(' 1234567890')
User_surname =input ('Please, enter your surname >>> ').upper().strip(' 1234567890')
letters_number = str(len(User_name))
greeting = 'Привіт, '
serlock_adress = greeting.replace('Привіт, ', 'Здоров, ')
result = serlock_adress + User_name + ' ' + User_surname + ', а ти знав, що твоє імя складється з ' + letters_number + ' літер'
print(f"{result}?")
