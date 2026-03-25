import random

play_again = True

while play_again:
    guessed_numbers = set()
    wrong_guesses = 0

    difficulty = input("Please type 'easy', 'medium', or 'hard': ")
    if difficulty == 'easy':
        random_number = random.randint(1, 50)
        max_guesses = 15    
    elif difficulty == 'medium':
            random_number = random.randint(1, 100)
            max_guesses = 10  
    elif difficulty == "hard":
                random_number = random.randint(1, 200)
                max_guesses = 5
    else:
        print("Invalid selection - Please type 'easy', 'medium', or 'hard")
        exit()


    while wrong_guesses < max_guesses:
        guess = int(input("Guess a number: "))
    
        if guess in guessed_numbers:
            print("You already guessed that number!")
            continue
    
        if guess > random_number:
            wrong_guesses += 1
            guessed_numbers.add(guess)
            print("Too High! Guess again.")
        
        elif guess < random_number:
            wrong_guesses += 1
            guessed_numbers.add(guess)
            print("Too low! Guess again.")
        
        else:
            print(f"Congratulations! You guessed the number {random_number}.")
            break
        
    else: 
            print(f"Game over! The number was {random_number}.")
            
    choice = input("Would you like to play again? y/n: ")
    if choice != 'y':
        play_again = False