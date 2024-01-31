import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
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
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def deposit():
    while True:
        amount = input("What is the amount you would like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than zero.")
        else:
            print("Please enter a Number.")

    return amount


def get_no_of_lines():
    while True:
        lines = input(f"Please Enter no of lines you would like to bet on from 1-{MAX_LINES} ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines")
        else:
            print("Please enter a Number.")

    return lines


def get_bet():
    while True:
        bet = input("How much would you like bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a Number.")

    return bet

    

def game(balance):
    lines_count = get_no_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = bet_amount*lines_count
        if total_bet > balance:
            print(f"Your total bet amount of ${total_bet} is greater than your remaining balance of ${balance}")
        else:
            break
    print(f"You are betting ${bet_amount} on {lines_count} lines each. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbols)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines_count, bet_amount, symbols_values)
    print(f"You won ${winnings}")
    print(f"You won on Lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your Current balance is {balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += game(balance)

    


main()
