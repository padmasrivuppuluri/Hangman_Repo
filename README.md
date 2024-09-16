# Hangman_Repo
## Project Description:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

### Task1:
1. Created a list variable for fruits.
2. Printed a random fruit from the list and assigned it to the word variable.

### Task2:
1. Created two functions: ask_for_input() and check_guess().
ask_for_input():
  - Prompts the user to enter a single letter.
  - If the input is not a single letter and not alphabetical, it displays an error message.
2. Validates that the input is exactly one character long and is an alphabetical letter.
check_guess():
  - Check if the entered letter is present in the word stored in the word variable.

### Task 3:
1. Created the Hangman class.
2. Implemented the __init__() method and added all the required attributes and parameters.
3. When the game starts, word_guessed should be initialized as a list of underscores (_) with the same length as the word. This indicates that no letters have been guessed yet.
4. num_letters: Represents the number of unique letters in the word that have not been guessed yet.
5. Defined 2 methods: ask_for_input() and check_guess()
   ask_for_input()
     - Prompts the user to enter a single letter.
     - If the input is not a single letter or is not alphabetical, it displays an error message.
     - If the input is a valid single character, it calls the check_guess() method.
     check_guess():
     - Checks if the entered letter is present in the word stored in the word variable. If so, it updates word_guessed by replacing underscores with the guessed letter (e.g., ['_', 'a', '_', 'a', '_', 'a'] if 'a' is guessed).
     - If the letter is not in the word, it prints an error message and decreases num_lives by 1.
     