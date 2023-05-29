import requests
from pprint import pprint

url = "https://dummyjson.com/users?limit=1000"

response = requests.get(url)

data = response.json()
users = data['users']
total_age = 0
total_number = 0
people_louisville = 0

for user in users:
    address = user.get('address', {})
    city = address.get('city', '')
    hair = user.get('hair', {})
    hair_color = hair.get('color', '')
    age = user.get('age', 0)
    gender = user.get('gender', '')
    if hair_color == 'Brown' and gender == 'male':
        total_age = total_age + age
        total_number = total_number + 1
    if city == 'Louisville':
        pprint(user)
if total_number:
    print('Середній вік чоловіків з Brown волоссям:', round(total_age / total_number, 0))
