with open('airport-codes.csv', mode='r', encoding='utf-8') as airports_code:
    content = airports_code.readlines()
    #print(content)
    for line in content:
        airport = line.strip().split(';')
        if airport[5] == 'UA':
            print(airport[2])