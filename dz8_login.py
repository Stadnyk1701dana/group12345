MSG_INPUT_LOGIN = ('Input login (use only letters): >>> ')
MSG_INPUT_PASSWORD = ('Password (use letters and numbers): >>> ')
MSG_CONFPASSWORD = ('Confirm password >>> : ')
LOG_SUCCESS = ('login successful. You are welcome!')
LOG_ERROR = ('Error. Password not confirmed. Try again!')
ER = ('Error!')

login1 = str(input(MSG_INPUT_LOGIN))
check_login = login1.isalpha()
if check_login != True:
    print(ER)
    login1 = input(MSG_INPUT_LOGIN)

password1 = input(MSG_INPUT_PASSWORD)
check_password1 = password1.isalnum()
if check_password1 != True:
    print(ER)
    password1 = input(MSG_INPUT_PASSWORD)
password2 = input(MSG_CONFPASSWORD)

if password1 == password2:
    print(LOG_SUCCESS)
    print('You were log out, because of teacher"s whims')
    login2 = str(input(MSG_INPUT_LOGIN))
    password3 = input(MSG_INPUT_PASSWORD)
    if login1 == login2 and password2 == password3:
        print(LOG_SUCCESS)
    else:
        print(LOG_ERROR)
else:
    print(LOG_ERROR)
