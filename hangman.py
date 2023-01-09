# pylint: disable=missing-module-docstring
import random
import string
from words_file import words


def get_valid_word(words_list):
    "This function choses a random and valid word from a list of words"
    # valid word -> free from spaces and hyphens (-)

    random_word = random.choice(words_list)
    while ' ' in random_word or '-' in random_word :
        random_word = random.choice(words_list)

    return random_word

def hangman():
    "This function implements the hangman game"

    guess_word = get_valid_word(words)

    print(guess_word)

    guess_letter = set(guess_word) # transform sto a character's list
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # To track which letters the user has choosed / guessed

    lives = 6

    while len(guess_letter) > 0  and lives > 0:
        print('You have used these letters : ', ' '.join(used_letters))
        current_guess = [letter if letter in used_letters else '-' for letter in guess_word ]
        print("Current word :", ' '.join(current_guess))

        user_letter = input(f'You got {lives} lives. Guess a letter\'s word : ').lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in guess_letter:
                guess_letter.remove(user_letter)
            else:
                lives = lives - 1
                print(f"{user_letter} not in the word.")

        elif user_letter in used_letters:
            print(f'You have already guessed this letter {user_letter}. Try again.')

        else:
            print("Invalid character ! Try again.")

    if len(guess_letter) > 0:
        print(f'You Lost : The word was {guess_word.upper()}')
    else:
        print(f'You nailed it ! you guessed the word : {guess_word.upper()}')


hangman()
