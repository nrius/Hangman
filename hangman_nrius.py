from IPython.display import clear_output
import random
import time


def add_attempt(guess_int, list_attemptted_letters_int):
    '''
    check for already used letters
    if letter is old,return previous list of used letters
    if letter is new, append it to the list of used letters
    '''
    
    if guess_int not in list_attemptted_letters_int:
        list_attemptted_letters_int.append(guess_int)
        return list_attemptted_letters_int
    
def num_ocurrencies(guess_int, word_int):
    '''
    return the number of instances a guess is find in the word
    '''
    
    return word_int.count(guess_int)

def word_lister(word_int): 
    '''
    divide the string word in a list of strings
    '''
    w_space_int=[]
    for w in word_int:
        w_space_int.append(w)  
    return w_space_int

def get_and_check_guess(list_attempt_int):
    
    '''
    Get the input letter(guess_int)
    check if it is ONE and LETTER
    otherwise complain and ask again
    convert to lowercase
    '''
    
    guess_int=str(input("write a letter please: "))
    status=False
    while status == False:
        
        if len(guess_int)>1:
            print("Only one character per guess. Your guess \""+guess_int+"\" is invalid.")
            guess_int =str(input("write ONE character please: "))
        elif guess_int.isalpha()==False:
            print("Only letters are valid guesses. Your guess \""+guess_int+"\" is invalid.")
            guess_int =str(input("a LETTER please: "))
        elif guess_int.lower() in list_attempt_int:
            print("your guess \""+guess_int+"\" has already been proposed")
            guess_int =str(input("write a NEW letter please: "))
        else:
            status=True

    print("Your guess is \""+guess_int.lower()+"\"")
    return guess_int  

def display(letters_strings_int, guess_int,stored_display_int,list_of_matches_int,list_attemptted_letters_int):
    
    '''
    for every letter in the word to guess,
    if it matches the guess(letter entered by user)
    appended in a list
    if it doesn't match append a "_"
    
    This creates a list (display_int) with the correct letters
    
    '''
    
    stored_display_int=[]
    
    
    for w in letters_strings_int:
        if w in list_attemptted_letters_int:
            stored_display_int.append(w) 
        else:
            stored_display_int.append("_")

    return (stored_display_int)


def choose_word():
    '''
    return a randomly choosen word from my list
    '''
    
    list_of_words_int = ['lambda', 'python', 'function','import','stackoverflow','syntaxerror']
    word_int = random.choice(list_of_words_int)
    
    return word_int

def game():
    
    '''
    Body of the game
    '''
    
    #get the word
    word=choose_word()
    
    #make the word into a list of strings (one string per letter)
    w_space=word_lister(word)
    total_letters=len(word)


    #set score to zero:
    total_attempts=0
    total_matches=0
    total_fails=0
    
    stored_display=[]
    list_attemptted_letters=[]
    list_of_matches=[]
    
    #print word length:
    print("Let's start. The word has",total_letters, "letters")
    print(hangm_pictures[total_fails])
     
    

    status_game=False
    while status_game==False:
        
        #get and chech if guess (input letter) is good
        guess=get_and_check_guess(list_attemptted_letters)
        list_attemptted_letters.append(guess)
    
        #update the total attemps:
        total_attempts+=1
        
        #show results:
        show_display=display(w_space, guess, stored_display,list_of_matches,list_attemptted_letters)
        print(show_display)

        n_ocurrencies=num_ocurrencies(guess, word)

        if n_ocurrencies ==0:
            print ("your guess:",guess,"is not in in the word")
            total_fails+=1
            print(hangm_pictures[total_fails])

        else:
            print ("your guess:",guess,"is", n_ocurrencies, "time(s) in the word")
            total_matches+=n_ocurrencies
            print(hangm_pictures[total_fails])

            
        #set occurencies to zero:
        n_ocurrencies=0
        
        print("so far you have: attempts:", total_attempts,"matches:",total_matches,"and fails:", total_fails)
        

        #End the game if:
        if total_matches>=total_letters:
            print("You won! The word was: ",word," !!!")
            print(hangm_pictures[8])
            print("You are free! I know, this is a strange justice system, but YAY!")
            status_game=True
           
        elif total_fails>=7:
            print(hangm_pictures[7])
            print("I am sorry! You lost!The word was: ",word)
            status_game=True
        
        clear_output(wait = True)

        #images
    
hangm_pictures = ['''    
   +---+
       |
       |
       |
       |
       |
=========''','''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
      |
      |
  O   |
 /|\  |
 / \  |
========='''
        ]

game()