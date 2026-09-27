def guess_number():
    import random 
    number_to_guess = random.randint(1, 100)
    if number_to_guess == 24:
        print("You guessed the number 24!")
    elif number_to_guess < 24:
        print("Ops too low!")
    elif number_to_guess > 24:
        print("Too high!")
    elif number_to_guess < 0:
        print("Please enter a number greater than 0")
    elif number_to_guess > 100:
        print("Please enter a number less than 100")

    return number_to_guess

def main():
    input("Guess any number between 1 to 100!")
    guess_number()
    
    
main()

    