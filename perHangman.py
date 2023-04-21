import random

def play_game():
    words = ("apple", "pear", "orange", "banana")
    word = random.choice(words)
    print(word)
    right_guesses = []
    wrong_guesses = []
    num_wrong_guesses = 0

    while True:
        display_word= " "
        for letter in word:
            if letter in right_guesses:
                display_word += letter
            else: 
                display_word += "_"
        print(f"\nSecret Word: {display_word}\n")

        guess = input("Guess the secret word: ")
        if guess in right_guesses:
            print(f"\ncorrect, but The letter {guess} is already been guessed")
            print("Try a new letter.")
        elif guess in word:
            print("correct")
            right_guesses.append(guess)
        elif guess in wrong_guesses:
            print(f"\ninccorrect and The letter {guess} is already been guessed")
            print("Try a new letter.")
        elif guess not in word:
            print("inccorrect")
            wrong_guesses.append(guess)
            num_wrong_guesses += 1

        if num_wrong_guesses >= 5:
            print("Sorry, You Lose !!!")
            break
        if set(word) <= set(right_guesses):
            print(f"\nYou guesses it, You win \n The secret word in {word}")
            break
        
    play_agian()


def play_agian():
    if input("play again? y/n: ").lower() == "y" :
        play_game()
    else: 
        exit()

play_game()