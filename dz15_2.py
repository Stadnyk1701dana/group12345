def miles_kilomiters(miles:float):
    if miles < 0:
        raise ValueError
    kilomiters = round(miles * 1.609344, 3)
    return kilomiters

miles = float(input('Введіть милі: '))
print(miles_kilomiters(miles))

def sorted_tuple(my_list:list):
    list_len = len(my_list)
    my_list.sort()
    for el in range(1,list_len):
        if my_list[el-1] > my_list[el]:
            raise ValueError
    tuple_sorted = tuple(my_list)
    return tuple_sorted


my_list = [6, 768, 0.874, 10, 12345]
print(sorted_tuple(my_list))