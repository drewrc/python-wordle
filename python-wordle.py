from random import choice
from words import word_list

start_game = "Play Wordle\n"
make_guess = "Enter your guess:\n"
total_guesses = 6


#ANSI COLOR KEY 
#\033 is the escape character that signals the beginning of an escape sequence.
# 1 after the escape character sets the style to bold.
# 30 sets the text color to black.
# 31 sets the text color to red.
# 32 sets the text color to green.
# 33 sets the text color to yellow.
# 42 sets the background color to green.
# 43 sets the background color to yellow.
# 47 sets the background color to white.
#\033[0m resets the style and colors



def player_guess(guess, answer):
    wordle = []
    letters_guessed = []
    # enumerate returns an iterator of tuples containing indices and values from an iterable object, such as a string, list, or tuple
    #ie. creates index 0123... for word
    for i, letter in enumerate(guess):

        #if guess is in correct position and correct place
        if answer[i] == guess[i]:
            letters_guessed.append(f"\033[1;30;42m{letter}\033[0m") # black on green background
            # '#' is placeholder for letter 
            wordle.append(f"\033[1;32m#\033[0m")

        #if letter guessed is correct, but NOT in correct place
        elif letter in answer:
            letters_guessed.append(f"\033[1;30;43m{letter}\033[0m") # black on yellow background
            # '*' letter guessed present in the chosen word, but not in the correct position
            wordle.append(f"\033[1;33m*\033[0m") # yellow
        
        #if letter is INCORRECT
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
        # .strip() removes whitespace 
        guess = input(make_guess).strip().upper()
        # is a while loop that continues to run as long as the length of the guess variable is truthy
        
        #len() = return the length (the number of items) of an object
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                print("\033[1;31mYou've already guessed this word!!\033[0m") #red
            else:
                print("\033[1;31mPlease enter a 5-letter word!!\033[0m") #red
            guess = input(make_guess).strip().upper()
        #append to array 
        already_guessed.append(guess)
        #function with two arguments, guess and chosen_word, and assigns the return values of the function to the variables guessed and pattern
        guessed, pattern = player_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)
        
        #* s used to unpack the list of words guessed and pass each element as a separate argument to the print()
        #sep by default is a single space, sep="\n" makes it =\n
        print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == total_guesses:
            end_of_game = True

    #end - if length of #player guesses = max guesses and guess does NOT = chosen word...
    if len(already_guessed) == total_guesses and guess != chosen_word:
    #display WORDLE X/# and correct word...
        print(f"\033[1;31mWORDLE X/{total_guesses}\033[0m") #red
        print(f"\033[1;32mCorrect Word: {chosen_word}\033[0m") #green
    else:
    #{len(already_guessed)} = # player guesses
    #{total_guesses} = max # of guesses 
        print(f"\033[1;32mWORDLE {len(already_guessed)}/{total_guesses}\033[0m")#green
    print(*full_wordle_pattern, sep="\n")

if __name__ == '__main__':
    print(start_game)
    #choice() ->  random element from the non-empty sequence
    chosen_word = choice(word_list).upper()
    game(chosen_word)
