import random
word_list = ["Apple", "Strawberry", "Cherry", "Grapes", "Banana"]
def ask_for_input():
    while True:
        guess = input("Enter the single letter")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    if guess.lower() in word.lower():
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

print(word_list)
word = random.choice(word_list)
print(word)
guess = ask_for_input()

        
    
