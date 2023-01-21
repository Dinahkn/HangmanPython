
#Dictionnary of hangman
HANGMAN_PHOTOS={
    0:"""
    x-------x
    """,
    1:
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    2:
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    3:
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    5:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    
    """    
    }

#welcome screen
def welcome_screen():
    HANGMAN_ASCII_ART=("""  _   _                                          
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __   
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
 |  _  | (_| | | | | (_| | | | | | | (_| | | | | 
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    |___/                        
                    """)
    print( HANGMAN_ASCII_ART)

#print the hangman of number tries
def print_hangman(num_of_tries):  
    return HANGMAN_PHOTOS[num_of_tries]

#choose the secret word
def choose_word(file_path, index):
    lines = open(file_path).readlines() 
    line = lines[0] 
    words = line.split()
    while index>len(words):
        index-=len(words)+1
    myWord=words[index]
    setWords=set(words)
    answer=(len(setWords),myWord)
    return myWord
 
#show the hidden word
def show_hidden_word(secret_word, old_letters_guessed):
    guess=""
    if len(old_letters_guessed)>0:
        for i in range(len(secret_word)):
            if secret_word[i] in old_letters_guessed:
                guess +=secret_word[i]+" "
            else:
                guess += "_ "
    else:
        guess="_ "*len(secret_word)
    return guess

#check the input
def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed=letter_guessed.lower()
    isGuessed=False
    for element in old_letters_guessed:
        if element==letter_guessed:
            isGuessed=True
    if ((letter_guessed.isalpha()) and (len(letter_guessed)==1) and isGuessed==False):
        return True
    else:
        return False

#check if we can put the letter in the list
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed=letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed)==True:
        return True
    else:
        print("X") 
        return False

#check if the user find the word
def check_win(secret_word, old_letters_guessed):
    count = 0
    for letter in old_letters_guessed:
        if letter in secret_word:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False

#check if the letter guessed is in the word 
def inWord(secret_word,letter_guessed):
    for l in secret_word:
        if letter_guessed==l:
            return True
    return False


def main():
    welcome_screen()
    file_path=input("Enter file path : ")
    index=int(input("Enter index : "))
    secret_word=choose_word(file_path,index)
    num_of_tries=0
    MAX_TRIES=6
    old_letters_guessed=[]
    print("Let's start!")
    while(num_of_tries<=MAX_TRIES):
        print(print_hangman(num_of_tries))
        print(show_hidden_word(secret_word,old_letters_guessed))
        letter_guessed=input("Guess a letter: ")
        
        if(try_update_letter_guessed(letter_guessed,old_letters_guessed)==False)or (inWord(secret_word,letter_guessed)==False):
            old_letters_guessed.append(letter_guessed)
            old_letters_guessed.sort()
            for element in old_letters_guessed:
                if old_letters_guessed.index(element)==(len(old_letters_guessed)-1):
                    print(element)
                else:
                    print(element,end=" -> ")
            num_of_tries+=1
        else:
            old_letters_guessed.append(letter_guessed)
        if check_win(secret_word,old_letters_guessed)==True:
            print("The secret word is : "+secret_word)
            break

    if (check_win(secret_word,old_letters_guessed)==True):
        print("WIN")

    else:
        print("LOSE")




main()