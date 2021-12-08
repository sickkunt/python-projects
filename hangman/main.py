import random
import string

def hangman_main():

    fruit_list = ['apple','banana','citrus','durian','eggplant','fig','watermelon'] #list can be imported

    random_word = random.choice(fruit_list)
    split_word = split(random_word)
    list_to_be_filled = ['_'] * len(random_word)
    missing_letters = 0
    already_guessed = 0
    alphabet = set(string.ascii_lowercase)

    print('Welcome to Hangman. The objective of the game is the guess the letters of a randomly chosen word.')

    difficulty = input("Enter a difficulty from 'easy', 'medium', or 'hard': ").lower()
    while not_difficulty(difficulty):
        difficulty = input("Difficulty can only be 'easy', 'medium', or 'hard'.\nEnter a difficulty from 'easy', 'medium', or 'hard': ").lower()

    lives = set_lives(difficulty)
    if lives == 666:
        print('Get fucked cunt')
        quit()

    print(f'This word has {len(random_word)} letters. You have {lives} lives.')
    print(list_to_be_filled)

    while list_to_be_filled != split_word and lives > 0:
        guess = input('Guess a letter: ').lower()
        while guess not in alphabet:
            guess = input('Guess has to be a letter. Guess a letter: ').lower()
        for i in range(0, len(split_word)):
            if guess == split_word[i]:
                if guess == list_to_be_filled[i]:
                    already_guessed = 1
                else:
                    list_to_be_filled.pop(i)
                    list_to_be_filled.insert(i, guess)
            elif guess != split_word[i]:
                missing_letters += 1
        if already_guessed == 1:
            already_guessed = 0
            print(f'Letter {guess} has already been guessed')
        elif missing_letters == len(split_word):
            lives -= 1
            missing_letters = 0
            print(f'The word does not have the letter {guess}. You have {lives} lives left.')
        else:
            print(list_to_be_filled)

    if lives == 0:
        print('You are out of lives! Better luck next time.')
    else:
        print(f"You have guessed the word '{random_word}' correctly!")

def split(word):
    return list(word)

def set_lives(difficulty):
    if difficulty == 'easy':
        return 12
    elif difficulty == 'medium':
        return 6
    elif difficulty == 'hard':
        return 3
    elif difficulty == 'fuck you':
        return 666

def not_difficulty(difficulty):
     if difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard' and difficulty != 'fuck you':
         return True

if __name__ == '__main__':
    hangman_main()
