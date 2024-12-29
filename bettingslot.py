# This is a simple betting slot machine game where the user can deposit money and play the game.
# The user can choose the number of lines to play and the amount to bet on each line.
# The user can play the game until they run out of money or choose to quit.
# The user can also make a deposit if they run out of money and continue playing the game.
# The user can win money if they get the same symbol on all the lines.
# The user can win money based on the value of the symbol and the amount they bet.
# The user can win money on multiple lines if they get the same symbol on all the lines.
# The user can win money on multiple lines if they get the same symbol on all the lines.


#Author: [   ... .- -. .--- .- -.--   ]


import random

MAXLINE=3
MAXBET=1000
MINBET=1
ROWS=3
COLS=3

symbol_count ={
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

def check_winner(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbolcheck=column[line]
            if symbolcheck != symbol:
                break
        else:
            winnings+=values[symbol]*bet
            winning_line.append(line+1)
    
    return winnings,winning_line
  




def slot_machine_spin(rows  ,cols,symbols):
    all_symbols = []
    for symbol,symbol_count  in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        
    columns=[]
   
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _  in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for _ in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[_],end=" | ")
            else:
             print(column[_],end=" ")
        print()



def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
             break
            else:
                print("Amount must be greater than 0")
            
        else: 
            print("Invalid amount")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to play: ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAXLINE:
                break
            else:
                print("Lines must be between 1 and "+str(MAXLINE)+"")
        else:
            print("Invalid number of lines")
    return lines
def betamount():
    while True:
        bet = input ("Enter a amount between("+str(MINBET)  + "-" + str(MAXBET)+") to bet on each line : ")
        if bet.isdigit():
            bet=int(bet)
            if MINBET <= bet <= MAXBET:
                break
            else:
                print("The bet amount must be between "+str(MINBET) +"-"+ str(MAXBET)+"")
        else:
            print("Invalid bet amount")
            
    return bet

def run(balance):
    lines=number_of_lines()
   
    while True:
        bet=betamount()
        total_bet=lines*bet
        if total_bet > balance:
            print(f"You do not have enough money to make this bet ,  your baance is ${balance}")
        else:
            break
        
    
    
    print(f"Your are betting ${bet} on each of the {lines} lines , total bet is ${total_bet}")
    
    spin=input("Press enter to spin the slot machine")
    print()
    
    slots = slot_machine_spin(ROWS,COLS,symbol_count)
    printslot = print_slot_machine(slots)
    winnings ,winning_line= check_winner(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}")
    print("you won on lines:",*winning_line)
    return winnings-total_bet
    

def retry(balance):
        val=0
        if balance <= 0:
            print("You have no money left")
            ans=input("press enter to make a deposit or q to quit")
            if ans.lower() == "q":
                print("you have left with $",balance)
                print("Thank you for playing")
                val=1
                
                
                 
            else:
           
                main()   
        return val 
                
                
           
def main():
    
    balance = deposit()
    while True:
        
        print(f"Your balance is ${balance}")
        
        play_again = input("press enter to play and q to quit ")
        if play_again.lower() == "q":
            break
        
        balance += run(balance)    
        re=retry(balance)
        if(re==1):
            break
 
main()








































