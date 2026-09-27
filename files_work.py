my_file = open("input.txt")       

for line in my_file:
    print(len(line))           
    print(line.strip())

my_file.close()

def count_words(file_name):
    try:

        my_file= open(file_name)
        for line in my_file:
            words = line.split()
        print(len(words))
        my_file.close()
    except:
        print('File not opened!')

    

def word_search(file_name, target_word):
    try:
        my_file = open(file_name)
        
        for line in my_file:
            words = line.split()
            if target_word in words:
                my_file.close()
                return True
        
        # Only return False AFTER the loop finishes checking ALL lines
        my_file.close()
        return False

    except FileNotFoundError:
        print("File not found!")
        return False

def longest_word(file_name):
    length = 0
    the_word =''
    my_file = open(file_name)
    for line in my_file:
        words = line.split()
        for word in words:
            if len(word)> length:
                length = len(word)
                the_word = word
    my_file.close()
    return length, the_word            

def main():
    count_words(r"C:\Users\T14S\Documents\GCISpython\input.txt")
    word_search(my_file , 'hi')
main()
