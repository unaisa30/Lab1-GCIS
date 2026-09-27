#how to handle runtime errors properly using try ans except:
actual_username = 'alfia'
actual_password = 'unaisa'
def validate(username, password):
    if actual_username == username and actual_password == password:
        print('Login success!')
    else:
        raise ValueError('Incorrect username or password!') 

def login():
    attempts = 4
    while True:
        username = input('please enter your username:   ')
        password = input('Please enter your password:   ')

        try:
            validate(username, password) 
            break    
        except ValueError as ve:
            attempts -= 1
            if attempts > 0:
                print('Invalid entry!')
            else:
                raise ve

def main():
    try:
        login()
    except:
        print('Login unsuccesful')
main()






def guessing_game():
    number = input('Guess the number: ')
    number = int(number)
    if number < 1 and number > 20:
        raise ValueError('invalid guess!')
    

def exceptions(number):
    try:
         number = int(input('please enter any number: '))
         return number**2
    except:
     print('invalid input')


def main():
    print(exceptions('three'))

main()

try:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))

    print('x/y is ', (x/y))

except ValueError:
    print('You have entered the wrong value. Please try again.')
except ArithmeticError:
    print('You cant divide by zero. Please try again. ')







