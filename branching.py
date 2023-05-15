user_age = int(input('Enter your age (int value) >>>'))

true = True
false = False

print(bool(user_age))
print(bool(0))
print(bool(1))
print(bool(' '))
print(bool('user_age' ))

if user_age:
    print('*')

if ' ':
    print('/')

print(user_age)
