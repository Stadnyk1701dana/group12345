import pytest
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