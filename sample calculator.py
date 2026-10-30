print("******Sample Calculator******")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

choice = int(input("Enter your option: "))
def add(num1, num2):
    print("addition",num1+num2)

def sub(num1, num2):
    print("subtraction",num1-num2)

def mul(num1, num2):
    print("Multiplication",num1*num2)

def div(num1, num2):
    print("division",num1/num2)
    
if choice>0 and choice<5:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))


if choice == 1:
    add(num1, num2)

elif choice == 2:
    sub(num1, num2)

elif choice == 3:
    mul(num1, num2)

elif choice == 4:
    div(num1, num2)

elif choice == 5:
    print("Exit")

else:
    print("Invalid option")



