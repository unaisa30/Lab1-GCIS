# Day and Date : Thursday 17/9/2026

c = 'A'
print(ord(c))    #prints our ACII code
new_char = ord(c) + 32 + 7
print(new_char)

def encrypt_letter(letter,key):
   return chr(ord(letter)+ key)
    

ASCII_FOR_0 = 48
ASCII_FOR_9 = 57


def encrypt_letter(letter,key):
    if letter.isalnum():
        if ASCII_FOR_0<=ord(letter)<=ASCII_FOR_9:
            if int(letter)+key>9:
                return chr(ord(letter)+key-10)
            else:
                return chr(ord(letter)+key)
    else :
        return "only works for alpha numerical numbers"    


def main():

    for i in range(100):
        print(i)

    for i in range(0,101):
        print(i)

    c=0
    while c<= 100:
        print(c)
        c = c+1

    for i in range(100,-1,-10):
        print(i)

    s = 'SKYWALKER'

    for i in range(len(s)):
        print(s[len(s)]-i)






    print(encrypt_letter('A', 7))
    print(encrypt_letter('B', 7))
    print(encrypt_letter('C' , 7))

main()    



    

