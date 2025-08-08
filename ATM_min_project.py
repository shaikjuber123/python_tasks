def credit():
    global balance
    amount = float(input("Enter amount to credit: "))
    if amount <= 0:
        print("Please enter a positive amount.")
    else:
        balance += amount
        print(f"${amount} credited to your account.")
        
def debit():
    global balance
    amount = float(input("Enter amount to debit: "))
    if amount <= 0:
        print("Please enter a positive amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"${amount} debited from your account.")
        
def Balance():
    global balance
    print(f"Your current balance is: ${balance}")
    
def exit():
    print("Thank you for using the ATM. Goodbye!")
    
balance=0
while True:
    print('''
    WELCOME TO ATM 
      MENU
    1.Credit
    2.Debit
    3.Balance
    4.Exit'''
    )
    choice=int(input('enter your choice(1-4):'))
    if choice==1:
        credit()
    elif choice==2:
        debit()
    elif choice==3:
        Balance()
    elif choice==4:
        exit()
        break
    else:
        print('Invalid choice. Please try again.')   


    
        