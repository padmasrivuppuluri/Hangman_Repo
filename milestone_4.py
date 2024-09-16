import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #List of fruits
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
        self.num_letters = [ ]
        for word_char in self.word[::]:
            if word_char not in self.num_letters:
              self.num_letters.append(word_char)
        print("Number of Uniques letters", len(self.num_letters))

    #In check_guess(): Replacing the '_' with word_guessed[index], else we are decresing the num_lives 
    def check_guess(self,guess):
        if guess.lower() in self.word.lower():
            print(f'Good guess! {guess} is in the word.')
            for index,letter in enumerate(self.word):
                if letter.lower() == guess.lower():
                    self.word_guessed[index] = guess 
            print(self.word_guessed)       
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives = self.num_lives - 1
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
          
word_list = ["Apple", "Strawberry", "Cherry", "Grapes", "Banana"]
print(word_list)

game=Hangman(word_list,5)
game.ask_for_input()

            
      

    



        
        