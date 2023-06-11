def return_list(user_number):
    if user_number < 1:
        raise ValueError
    list_comp = [element+1 for element in range(user_number-1, user_number+9)]
    return list_comp

user_number = int(input('Введіть ціле додатнє число: '))
print(return_list(user_number))

