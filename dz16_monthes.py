def change_monthes():
    list_monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = 0
    while list_monthes[month] != 'new month':
        print(list_monthes[month])
        month = month + 1
        if month == 11:
            month = 0
    return list_monthes


result = change_monthes()


