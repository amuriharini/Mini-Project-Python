print("ATM Simulation Using Functions")
print("1.Check Balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")

balance=10000
option=int(input("Select an option"))

if option in[2,3]:
    amount=int(input("enter an amount: "))

def checkbalance():
    print("balance=",balance)


def deposit(amount):
    print("deposit",balance+amount)

def withdraw(amount):
    if amount<=0:
        print("negative amount not accepted")
    elif amount==0:
        print("zero amount is not accepted in withdrawel")
    else:
        print(balance-amount)
        
if option==1:
    checkbalance()
    
elif option==2:
    deposit(amount)
    
elif option==3:
    withdraw(amount)

elif option==4:
    print("exit")













