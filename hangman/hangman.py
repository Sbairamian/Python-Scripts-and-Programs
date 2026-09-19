import random

from hangman_art import stages
from hangman_words import hangman_words
from hangman_art import logo



word_list = hangman_words

lives = 6



print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    print(guessed_letters)



    if guess in guessed_letters:
        if guess in chosen_word:
            print(f"You already guessed the letter {guess}")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, {guess} is not in the word.  You lose a life.")

        if lives == 0:
            game_over = True

           
            print(f"***********************YOU LOSE********************** \n The correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])
