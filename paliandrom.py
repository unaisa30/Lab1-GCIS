def paliandrom(word):
    for i in range(len(word//2)):
        if word[i].lower()!=word[(-1)-i].lower():
            return False
        else:
            return True
        

def main():
   s1 = 'Ana'
   s2 = 'ANNA'
   s3 ='alfia'
main()
