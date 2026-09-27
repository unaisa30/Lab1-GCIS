def number_to_letter_grade(number):

    if(type(number)== int or type(number)== float):
        if number >= 92:
            return '+A'
        elif number >= 89 and number < 92:
            return 'A'
        elif number >= 86 and number < 89:
            return '+B'
        elif number >= 82 and number < 86:
            return 'B'
        elif number >= 79 and number < 82:
            return '-B'
        elif number >= 76 and number < 79:
            return '+C'
        elif number >= 72 and number < 76:
            return 'C'
        elif number >= 69 and number < 72:
            return '-C'
        elif number >= 59 and number < 69:
            return 'D'
        elif number >= 0 and number < 59:
            return 'F'
        elif number < 0 :
            return 'OUT OF RANGE'
    else:
        return 'wrong input, please enter a number.'   

def main():
    print(number_to_letter_grade(96))
main()

def letter_to_gpa(grade):
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    else:
        return -1

def main():

    grade1 = input('Type your first grade: ').upper()
    grade2 = input('Type your second grade: ').upper()
    grade3 = input('Type your third grade: ').upper()
    grade4 = input('Type your fourth grade: ').upper()

    g1 = letter_to_gpa(grade1)
    g2 = letter_to_gpa(grade2)
    g3 = letter_to_gpa(grade3)
    g4 = letter_to_gpa(grade4)

    if g1 == -1 or g2 == -1 or g3 == -1 or g4 == -1:
        print("Wrong input")
    else:
        average = (g1 + g2 + g3 + g4) / 4
        print('Your average GPA is: ', average)
        

main()


    



    


