#Creating a list for Fruits
import random
word_list = ["Apple", "Strawberry", "Cherry", "Grapes", "Banana"]
guess = input("Enter the single letter ")
if len(guess) ==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
print(word_list)
word = random.choice(word_list)
print(word)