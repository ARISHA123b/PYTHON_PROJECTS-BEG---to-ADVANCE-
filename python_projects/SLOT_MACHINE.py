import random 

MAX_LINES = 3 #GLOBAL VARIABLE 
MAX_BET = 100 
MIN_BET = 1 

ROWS = 3 
COLUMNS = 3 

SYMBOLS_count = {
    "A":2 ,
    "B":4,
    "C":6,
    "D":8
}
def get_slot_machine_spin(rows, cols , symbols):
    all_symbols = []
    for symbols , SYMBOLS_count in symbols.items():
        for _ in range(SYMBOLS_count): # ananoymous variable in python 
            all_symbols.append(symbols)
    COLUMNS = []
    for col in range(cols):
        columns = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(value)
        COLUMNS.append(cols)
    return COLUMNS
def print_slot_machine(columns):
    # transposing matrix 

    for row in range(len(column[0])):
        for column in columns:
             for i , char in enumerate(columns):
                 if i != len(columns)-1:
                     print(column[row],"|")
                 else:
                    print(column[row])



def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 ")
        else:
            print("please enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the no  : of lines to bet (1-"+str(MAX_LINES) + ")? $:")# ADDED MAX LINES INSIDE OF THE STRING 
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
               break
            else:
               print("Enter a valid of numbers.")
        else:
           print("Please enter a Number :")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be betwenn $ {MIN_BET} - ${MAX_BET} .")
        else:
           print("Enter a valid Number")
    return amount




def main():
    balance = deposit() # amount will the deposiit
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
            
        TOTAL_BET = bet * lines 
        if TOTAL_BET > balance:
            print(f"you dont have enough balance to bet that amount you current balance is {balance} ")
        else:
            break

    
    print(f"you are betting $ {bet} on {lines} lines . TOtal bet is equal to {TOTAL_BET}")

main()