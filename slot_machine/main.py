# random module -> This module implements pseudo-random number generators for various distributions.
import random

# adding global constants
# it is a constant value something that cannot change
# it is a convention to write constants in --> uppercase
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# now we want to specify how many rows and columns our slot machine would have
ROWS=3
COLS=3

# now we have to decide which symbols we want in our slot machine
# we going to use alphabets
# we will make a dictionary
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    # first we will check on the lines on which they have bet on
    # we are looping through each row we are going to be checking on which user will bet on
    for line in range(lines):
          symbol=columns[0][line] 
          # we can use for else 
          # if u break else statement will not print
          # if  break occurs in for loop this else statement will be printed
          for column in columns:
              symbol_to_check= column[line]
              if symbol != symbol_to_check:
                  break
          else:
              winnings += values[symbol] *bet
              winning_lines.append(line +1)
    return winnings,winning_lines
              
      





def get_slot_machine_spin(rows, cols, symbols):
    # this is going to be list
    all_symbols =[]
    # we will write a for loop to add all the symbols present with us into all_symbols list
    # since we are itterrating through a dictionary(symbol_count) we can do the following
    # when u use .items what it gives is both the key and value associated with the dictionary
    # key is symbol  and value is symbol_count
    # example
    # symbol will take A and symbol_count will take 2
    for symbol,symbol_count in symbols.items():
        # _ is the anonymous variable in python
        # so whenever you want to say loop through something,but you dont care about the count or itteration value then you can put underscore and you will not have an unused variable anymore
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # example of nested list
    #columns=[[],[],[]]
    # we start defining by our columns list
    columns=[]

    # this for loop is for generating a column
    for _ in range(cols):
        column=[]
        #we are copying the all_symbols list to another variable so that we can remove the variable once used for selection
        # for copying a list we are using : symbol is a  operator  knowns as slice opeartor
        current_symbols=all_symbols[:]
        for _ in range(rows):
                # random.choice will pick the random value from the current_symbols list
                value=random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    # this part of code is for printing the list from column wise to row wise
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        # empty print will print the new line    
        print()




# this function is responsible for collecting user input
def deposit():
# we will use while loop --> we will continue to ask deposit amount from the user and it will stop when user will give  a valid deposit amount
    while True:
        amount = input("what would you like to deposit? $")
        # now we have to check whether the amount user have type is a number or not?
        # isdigit function is used to check whether a string is a whole number or not
        if amount.isdigit():
            # now we will convert the string into integer using integer function
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


# this function is created to get the lines from the user on which they want to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of Lines to bet on (1-" + str(MAX_LINES) + ") ")
        # checking if lines enter by user to bet on , is a digit or not
        if lines.isdigit():
            # converting lines value as a string to --> integer
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of Lines.")
        else:
            print("Please enter a number.")
    return lines    


# this function is created to take the input from user on how much they want to bet
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
       
        if amount.isdigit():
           
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter a number.")
    return amount  




def main():
    balance= deposit()
    while True:
        print(f"curent balance is ${balance}")
        answer = input("Press Enter to Play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")




def spin(balance):
    #balance= deposit()
    lines = get_number_of_lines()
    # print(balance,lines)

     # we have apply this while loop and if condition to check whether the user have enough money to bet in his/her balance
    while True:
      bet=get_bet()
      total_bet = bet * lines

      if total_bet > balance:
          print(f"You do not have enough to bet that amount ,your current balance is: ${balance} ")
      else:
          break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")
    
    slots=get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on Lines:",*winning_lines)
    return winnings- total_bet

# to call a function we simply write the name of the function and after that paranthesis
main()
                


       
