import random

words = ["python", "hangman", "challenge", "programming", "assistant"]

word_to_guess = random.choice(words)

hidden_word = ["_"] * len(word_to_guess)

guessed_letters = set()
wrong_guesses = 0
max_guesses = 6

while wrong_guesses < max_guesses and "_" in hidden_word:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                hidden_word[i] = guess
                print("Well done! You guessed a letter!")
    else:
                wrong_guesses += 1
                print ("Sorry. Try again.")
                
if "_" not in hidden_word:
        print ("Well done! You guessed the word {word_to_guess}!")
        
else:
        print (f"Unlucky! The word was {word_to_guess}")