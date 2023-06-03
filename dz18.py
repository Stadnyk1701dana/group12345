def function(value):
    return value

def decorator_of_string(function, value):
    edited_result = ''
    result = function(value)
    if type(result) == str:
        edited_result = '<b>' + result + '</b>'
    return edited_result
print(decorator_of_string(function, 'Дана Стадник'))



