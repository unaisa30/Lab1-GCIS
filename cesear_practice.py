# Day and Date : Sunday 20/9/2026
#Practice at home :

# Implementing ceaser cipher:
# Also created a function that accepts only uppercase and returns an empty string if lowercase or special char.

def is_alphabetic(character):
    if character.isupper():
        return True
    else:
        return False

def is_lower_alphabet(character):
    if character.islower():
        return True
    else:
        return False


def encrypt_letter(letter, key):
    """ ord function converts letters to integer 
    and then we add it up with the key so that it 
    is shifted and at last we convert the whole thing
      to a letter which is stored on encrypted."""
    if is_alphabetic(letter):
        encrypted = chr(ord(letter) + key ) 
        return encrypted
    else:
        return '  '


    
def decrypt_letter(letter, key):
    if is_lower_alphabet(letter):
        decrypted = chr(ord(letter) - key )
        return decrypted
    else:
        return '  '

def encrypt_word(word, key):
    encrypted="" 
    for i in word:
        if (',' or '!' or '.' or ';') in word:
            continue
        new_letter=encrypt_letter(i, key)
        encrypted += new_letter
    return encrypted                             # always return outside for loop

def encyrpted_sentence(sentence, key):
    encrypted=""
    words= sentence.split()
    for i in words:
        new_word = encrypt_word(i,3)
        encrypted += new_word
    return encrypted



def main():
    to_encrypt = 'A'
    result1 = encrypt_letter(to_encrypt, 3)
    print(result1) 
    to_decrypt = 'f'
    result2 = decrypt_letter(to_decrypt, 3)
    print(result2)
    print(encrypt_word('ABC', 3))

    s1 = 'NICE TO MEET YOU GUYS!'
    print(encyrpted_sentence(s1, 3))   
if __name__ == "__main__":
    main()


    


