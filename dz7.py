#симулятор каси магазину
#код, наведений нижче, приймає від покупця наступну інформацію про закупівлю 2-х товарів
#- назва
#- кількість (ціле число)
#- ціна за одиницю
#на підставі отриманих даних формується чек
#всі ціни та вартість мають бути виведені в форматі з копійками, кількість - цілі числа
#програма розрахована на використання на території України

import textwrap
from datetime import datetime
from decimal import Decimal


# goods 1 section
MSG_INPUT_TITLE = 'Введіть назву товару {position}: >>> '
MSG_INPUT_QUANTITY = 'Введіть бажаєму кількість товару {position} : >>> '
MSG_INPUT_PRICE = 'Введіть бажаєму кількість товару {position} (два знаки після коми): >>> '
item_1_title = textwrap.shorten(input(MSG_INPUT_TITLE.format(position=1)).ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = int(input(MSG_INPUT_QUANTITY.format(position=1)))
item_1_zina = float(input(MSG_INPUT_PRICE.format(position=1)))

# goods 2 section
item_2_title = textwrap.shorten(input(MSG_INPUT_TITLE.format(position=2)).ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = int(input(MSG_INPUT_QUANTITY.format(position=2)))
item_2_zina = float(input(MSG_INPUT_PRICE.format(position=2)))

item_1_total_cost = Decimal(str(item_1_quantity)) * Decimal(str(item_1_zina))
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('0.0001'))

item_2_total_cost = Decimal(str(item_2_quantity)) * Decimal(str(item_2_zina))
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('0.0001'))

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'

# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
print(printing_template.format(item_1_title, item_1_quantity, item_1_zina, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, item_2_zina, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    item_1_quantity + item_2_quantity,
    'x',
    item_1_total_cost_right_format + item_1_total_cost_right_format
    )
)
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')
