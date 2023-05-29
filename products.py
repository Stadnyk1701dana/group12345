import requests

url = 'https://script.google.com/macros/s/AKfycbzfw7GYZfBTyswJ_y0gTnAVmz898yew7Ln5TjfYnUuNsCkwedsPIOF4jOs53RfBRLM/exec'

response = requests.get(url)

data = response.json()

products = data['products']
cost = 0
cost_nogluten = 0

for product in products:
    quantity = product.get('quantity', '')
    price = product.get('price', '')
    nogluten = product.get('nogluten', '')
    cost = cost + quantity * price
    if nogluten == True:
        cost_nogluten = cost_nogluten + quantity * price
print('Вартість усіх товарів:', cost)
print('Вартість товарів без глютену:', cost_nogluten)