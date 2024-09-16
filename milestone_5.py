import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #List of words
        self.word_list = word_list
        #Number of lives
        self.num_lives = num_lives
        #Getting the random word from the fruits list
        self.word=random.choice(word_list)  
        print(self.word)
        #A list of the letters of the word, with _ for each letter not yet guessed
        self.word_guessed = ['_' for _ in range(len(self.word))]  
        self.list_of_guesses =[]
        #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = set(self.word.lower()) - set(' ')

    def unique_letters(self):
        return len(self.num_letters)

    #In check_guess(): Replacing the '_' with word_guessed[index], else we are decresing the num_lives 
    def check_guess(self,guess):
        if guess.lower() in self.word.lower():
            print(f'Good guess! {guess} is in the word.')
            for index,letter in enumerate(self.word):
                if letter.lower() == guess.lower():
                    self.word_guessed[index] = self.word[index] 
            self.num_letters.discard(guess)
            print(' '.join(self.word_guessed))      
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')

    '''In ask_for_input function() Asking the user for the input
       Validating the input is whether single alphabatical character or not ''' 

    def ask_for_input(self):
        while True:
            guess = input("Enter the single letter")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
          
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.unique_letters() > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.unique_letters() == 0:
            print("Congratulations. You won the game!")
            break
word_list = ["Apple", "Strawberry", "Cherry", "Grapes", "Banana"]
play_game(word_list)
        

        
        

           



