import requests
from pprint import pprint

player = input("Player Username: ").lower()

headers = {
    "User-Agent": "My APP"
}

CHESS_API = "https://api.chess.com/pub/player/"
response = requests.get( CHESS_API + player, headers=headers).json()

data_keys = []

# accessing data from chess.com into a list
for keys in response:
    data_keys.append(keys)

print(f"Details of {player} on chess.com")
print("-"*15)
    
# printing data from list to terminal
for keys in data_keys:
    value = response[keys]
    print(f"{keys} : {value}")
