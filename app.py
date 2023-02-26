import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = f'https://api.apilayer.com/currency_data/list' 
 
headers = {'apikey': API_KEY}
r = requests.get(URL, headers=headers)

print(r.json())

print('Welcome to ConvertMyMoney!')

# Print list of currencies to convert

base_currency = input('Base Currency: ')
to_currency = input('To Currency: ')
amount = float(input('Amount: '))



