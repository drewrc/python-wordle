from random import choice
from words import word_list

start_game = "Play Wordle\n"
make_guess = "Enter your guess:\n"
total_guesses = 6

#player guess has two arguments - guess and answer
def player_guess(guess, answer):
    #set wordle = empty array 
    wordle = []
    #letters guessed to empty array
    letters_guessed = []
    for i, letter in enumerate(guess):
        #is letter at same index the same?
        if answer[i] == guess[i]:
            #append guessed letter to letters_guessed list
            letters_guessed.append(f"\033[1;30;42m{letter}\033[0m") # black on green background
            #append to wordle, style green, add ("#")
            wordle.append(f"\033[1;32m#\033[0m")
        #if letter is in answer
        elif letter in answer:
            letters_guessed.append(f"\033[1;30;43m{letter}\033[0m") # black on yellow background
            wordle.append(f"\033[1;33m*\033[0m") # yellow
        #if letter guessed 
        else:
            letters_guessed.append(f"\033[1;30;47m{letter}\033[0m") # black on white background
            wordle.append(f"\033[1;31m.\033[0m") # red
    #return join str
    return ''.join(letters_guessed), ''.join(wordle)

def game(chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        # ask user for input
        guess = input(make_guess).strip().upper()
        # is a while loop that continues to run as long as the length of the guess variable is truthy
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                print("\033[1;31mYou've already guessed this word!!\033[0m")
            else:
                print("\033[1;31mPlease enter a 5-letter word!!\033[0m")
            guess = input(make_guess).strip().upper()
        #append to array 
        already_guessed.append(guess)
        #function with two arguments, guess and chosen_word, and assigns the return values of the function to the variables guessed and pattern
        guessed, pattern = player_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)
        
        #* s used to unpack the list of words guessed and pass each element as a separate argument to the print()
        print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == total_guesses:
            end_of_game = True
    if len(already_guessed) == total_guesses and guess != chosen_word:
        print(f"\033[1;31mWORDLE X/{total_guesses}\033[0m")
        print(f"\033[1;32mCorrect Word: {chosen_word}\033[0m")
    else:
        print(f"\033[1;32mWORDLE {len(already_guessed)}/{total_guesses}\033[0m")
    print(*full_wordle_pattern, sep="\n")

if __name__ == '__main__':
    print(start_game)
    # choose a random word from the word list
    chosen_word = choice(word_list).upper()
    game(chosen_word)
