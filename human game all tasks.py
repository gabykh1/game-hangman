import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

HANGMAN_ASCII_ART = ("""
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/ 
let's go!""")
MAX_TRIES = "max mistakes: 6"



PICTURE_1 = 'x-------x'
PICTURE_2 = """
        x-------x
            |
            |
            |
            |
            |"""

PICTURE_3 = """
        x-------x
            |       |
            |       0
            |
            |
            |"""

PICTURE_4 = """
        x-------x
            |       |
            |       0
            |       |
            |
            |
        """

PICTURE_5 = """
        x-------x
            |       |
            |       0
            |      /|\\
            |
            |
        """

PICTURE_6 = """
        x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |
        """

PICTURE_7 = """
        x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |
        """
HANGMAN_PHOTOS = {1: PICTURE_1, 2: PICTURE_2, 3: PICTURE_3, 4:PICTURE_4, 5:PICTURE_5, 6:PICTURE_6, 7:PICTURE_7}

def opening_of_the_game():
    """
    print the screen the game starts on
    :return: none
    """
    print(f"{Fore.RED}A{Fore.GREEN}N{Fore.YELLOW}I{Fore.BLUE}M{Fore.MAGENTA}A{Fore.CYAN}L {Fore.RED}Q{Fore.GREEN}U{Fore.YELLOW}I{Fore.BLUE}Z")
    # it's printing animal quiz colorful
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)
def print_hangman(num_of_tries):
    """
    the picture state of the game based on the num of tries
    :param num_of_tries:
    :return: HANGMAN_PHOTOS[num_of_tries] out of the dictionary
    """
    return HANGMAN_PHOTOS[num_of_tries]


def check_win(secret_word, old_letters_guessed):
    """
    check if all the old letters are in the secret word and return true / false
    :param secret_word:
    :param old_letters_guessed:
    :return: True, False
    """
    if show_hidden_word(secret_word, old_letters_guessed) == secret_word:
        return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    check if all the old letters are in the secret word and show them, and fill the blank letters as '_' insted of the letter
    :param secret_word:
    :param old_letters_guessed:
    :return: (''.join(guessed_word))
    """
    guessed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

def check_valid_input(letter_guessed, old_letters_guessed):
    """
     check if the guesser's letter is a valid input
    :param letter_guessed:
    :param old_letters_guessed:
    :return: True, False
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    show the progress of guessing letters based on "check valid input" return + adding the letter to old_letter_guessed
    :param letter_guessed:
    :param old_letters_guessed:
    :return: none
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        print("the letter you choose: " + letter_guessed.lower())
        print('used letters: ', old_letters_guessed)
    else:
        print('X', '\n' + "->".join(old_letters_guessed), '\nFalse')

def choose_word(file_path):
    """
    choosing a random animal out of the file findme.txt
    :param file_path:
    :return: the secret word
    """
    with open(file_path) as words_file:
    # split the file to get animals mame
        words = words_file.read().strip().split(", ")
    return random.choice(words)


def main():
    opening_of_the_game()
    secret_word = choose_word(r'{findme.txt}')
    old_letters_guessed = []
    num_of_tries = 1
    while num_of_tries < 7:
        print(print_hangman(num_of_tries))
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input('choose a letter:')
        bool = check_valid_input(letter_guessed, old_letters_guessed)
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if not bool:
            continue
        if check_win(secret_word, old_letters_guessed):
            print(f"{Fore.BLACK}{Back.YELLOW}you won")
            print(show_hidden_word(secret_word, old_letters_guessed))
            break
        if letter_guessed not in secret_word:
            num_of_tries += 1
    if num_of_tries == 7:
        print(print_hangman(num_of_tries))
        print(f"{Fore.BLACK}{Back.RED}you lose :({Back.RESET}\n{Fore.BLACK}{Back.BLUE}the word was " + secret_word + " you can always win next time")
if __name__ == "__main__":
    main()