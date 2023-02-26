import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = f'https://api.apilayer.com/currency_data/' 
 
headers = {'apikey': API_KEY}
response = requests.get(f'{URL}list', headers=headers)

currencies = response.json()['currencies']


print('Welcome to ConvertYourMoney!\n')

print('Available currencies: ')
for code, currency  in currencies.items():
    print( code, ":", currency)
    
    
base = input('Base Currency: ')
to = input('To Currency: ')
amount = float(input('Amount: '))


convert_request = requests.get(f'{URL}convert?to={to}&from={base}&amount={amount}', headers=headers)

result = convert_request.json()['result']

print(f'{amount}{base} is {result}{to}.')

