from requests import get

BASE_URL = "https://data.fixer.io/api/"

'''API_KEY = "887456197b2279764393497757cde4d9"'''

API_KEY= input("Enter your fixer.io API key: ")

endpoint = f"latest?access_key={API_KEY}"

response = get(BASE_URL + endpoint).json()

all_currencies = response['rates']

all_currency_list = list(all_currencies.keys())

user_currency = input("Enter your currency: ").upper()
if user_currency not in all_currency_list:
    print("Invalid Currency!")
else:
    convert_to = input("Enter the currency to convert: ").upper()
    if convert_to not in all_currency_list:
        print("Invalid Currency!")
    else:
        amount = float(input(f"Enter the amount in {user_currency}: "))

        user_currency_rate = all_currencies[user_currency]
        convert_currency_rate = all_currencies[convert_to]

        converted_amount = (amount / user_currency_rate) * convert_currency_rate

        print(f"{amount} {user_currency} == {converted_amount:.2f} {convert_to}")
