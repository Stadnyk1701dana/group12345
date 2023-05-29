#import pytest
import test_library
def test_number_is_int():
    test_value = 5
    assert test_library.is_int(test_value) is True


#def is_fractional():
#    test_value1 = 10
#    assert test_library.is_fractional(test_value1) is True

def is_positive():
    test_value2 = 88
    assert test_library.is_positive(test_value2) is True

def is_negative():
    test_value3 = 25
    assert test_library.is_negative(test_value3) is True

print('test_number_is_int: ', test_number_is_int())

print('is positive: ', is_positive())

#def test_number_is_not_even()

def miles_kilomiters(miles:float):
    if miles < 0:
        raise ValueError
    kilomiters = round(miles * 1.609344, 3)
    return kilomiters

miles = float(input('Введіть милі: '))
print(miles_kilomiters(miles))

def sorted_tuple(my_list):
    list_len = len(my_list)
    my_list.sort()
    for el in range(1,list_len):
        if my_list[el-1] > my_list[el]:
            raise ValueError
    tuple_sorted = tuple(my_list)
    return tuple_sorted



my_list = [6, 768, 0.874, 10, 12345]
print(sorted_tuple(my_list))