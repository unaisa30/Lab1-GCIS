

def choose_operation():
    print("Welcome to the Python Calculator!")
    print("Which operation would you like to perform?")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")  
    print("4- Division")
    choice = input("Enter your choice: ")
    return choice


def addition(a,b):
    return float(a) + float(b)

def subraction(a,b):
    return float(a) - float(b)

def multiplication(a,b):
    return float(a) * float(b)

def division(a,b):
    return float(a) / float(b)

def main():
    choice = choose_operation()

    if choice == "1":
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        result = addition(a,b)
        print("The result is:", result)
    elif choice == "2":
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        result = subraction(a,b)
        print("The result is:", result)
    elif choice == "3":
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        result = multiplication(a,b)
        print("The result is:", result)
    elif choice == "4":
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        result = division(a,b)
        print("The result is:", result)

main()


