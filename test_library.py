def is_int(test_value) -> bool:
    remain_part = float(test_value) % 1
    result = remain_part == 0
    return result


#def is_fractional(test_value1) -> bool:
#    remain_part = float(test_value1) % 1
#    if remain_part != 0:
#        result = remain_part
#        return result


def is_positive(test_value2) -> bool:
    result = test_value2 >= 0
    return result


def is_negative(test_value3) -> bool:
    result = test_value3 <= 0
    return result