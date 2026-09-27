# Day and Date : Sunday 20/9/2026

import cesear_practice

def test_encrypt_letter():
    #setup
    letter = 'A'
    key = 3
    expected = 'D'

    #invoke 
    actual = cesear_practice.encrypt_letter(letter, key)

    #analyse
    assert actual == expected

def test_cesear_practice():
    #setup
   char = 'A'

    #invoke
   result = cesear_practice.is_alphabetic(char)

    #analyse
   assert result == True

def test_decrypt_letter():
    #setup
    letter = 'f'
    key = 3
    expected = 'c'

    #invoke
    actual = cesear_practice.decrypt_letter(letter, key)

    #analyse 
    assert actual == expected





    
