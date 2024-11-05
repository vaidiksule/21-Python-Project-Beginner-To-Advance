import random as rd

MAX_LINES = 3
MAX_BET = 100

ROWS = 3
COLUMN = 3
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
}
symbol_values = {
    "A" : 6,
    "B" : 4,
    "C" : 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = rd.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Enter deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter no of lines you want to bet on (1-" + str(MAX_LINES) + ") :")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines should be between 1 to {str(MAX_LINES)}.")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        bet = input("What would you like you bet on each line?(1-" + str(MAX_BET) + ") : $")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= MAX_BET:
                break
            else:
                print(f"Betting amount should be between 1 to {str(MAX_BET)}.")
        else:
            print("Please enter a number")

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet <= balance:
            print(f"You are betting ${bet} on {lines} line, so total betting amount = ${total_bet}")
            break
        else:
            print(f"Insufficient balance, your current balance is {balance}")
    
    slots = get_slot_machine_spin(ROWS, COLUMN, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You Won ${winnings}")
    print(f"You Won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to spin (q to quit)")
        if answer.lower() == "q":
            break
        balance += spin(balance)    

    print(f"You left with ${balance}")

main()