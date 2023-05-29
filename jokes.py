def tell_jokes(number):
    joke1 = '– Юро, скільки твоя мама повинна заплатити за 2 кілограми яблук, якщо 1 кг коштує 10 гривень? – Не можу сказати, учителю, моя мама завжди торгується'
    joke2 = '- А правда, що риба корисна для мозку? - Так, особливо рибалка - для розвитку уяви.'
    joke3 = '– Наш кіт птахів на вулиці ловить, а домашнього папугу чомусь не чіпає. – А ось якщо у тебе заначка вдома лежить, ти ж її теж не чіпаєш?!'
    if number == 1:
        smile = joke1
    if number == 2:
        smile = joke2
    else:
        smile = joke3
    return smile


number = int(input('Введіть число (1 - 3):'))
result1 = tell_jokes(number)
print(result1)


def perymetr(length, width):
    perymetr = float(2 * (length + width))
    return perymetr


length = float(input('Введіть довжину прямокутника:'))
width = float(input('Введіть ширину прямокутника:'))
result2 = perymetr(length, width)
print(result2)


def edit_str(user_str):
    edited_string = ''
    for str in user_str:
        if str == 'ї' or str == 'ж' or str == 'Ї' or str == 'Ж':
            str = ''
        edited_string = edited_string + str
    return edited_string


user_str = str(input('Введіть стрічку: '))
result3 = edit_str(user_str)
print(result3)





