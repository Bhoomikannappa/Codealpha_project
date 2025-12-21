import random

def hungman_game():

    python_libraries = {
        "numpy": "A library for numerical computations in Python.",
        "pandas": "A library providing high-performance data manipulation and analysis tools.",
        "matplotlib": "A plotting library for creating static, animated, and interactive visualizations in Python.",
        "sklearn": "A machine learning library for Python.",    
        "seaborn": "A statistical data visualization library based on matplotlib.",
        "opencv" : "A library for computer vision and image processing."
    }
    while True:
        print("\n" + "="*50)
        print("Welcome to the Python Libraries Hangman Game!")
        print("="*50)
        print("Guess the word letter by letter.")
        print("The words are names of popular Python libraries.")

        #select random word
        word = random.choice(list(python_libraries.keys()))
        clue = python_libraries[word]
        word = word.lower()

        word_length = len(word)
        guessed_word = ["_"] * word_length
        guessed_letters = []
        lives = 6
        wrong_guesses = 0

        print(f"Length of the word : {word_length}")
        print(f"Word : {' '.join(guessed_word)}")
        print(f"Lives remaining: {lives}")

        while True:
            
            guess = input("\nEnter a letter: ").lower()
            
            if guess =='quit':
                print("Thanks for playing!")
                return
            
            if len(guess) != 1:
                print("Please enter only ONE letter at a time!")
                continue
            if not guess.isalpha():
                print("Please enter a valid letter!")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")

                for i in range(word_length):
                    if word[i] == guess:
                        guessed_word[i] = guess
            
            else:
                lives -= 1
                wrong_guesses += 1
                print(f"Wrong guess! '{guess}' is not in the word.")
                print(f"Lives remaining: {lives}")

                if wrong_guesses % 2 == 0:
                    print(f"Clue: {clue}")

            print(f"Word : {' '.join(guessed_word)}")
            if guessed_letters:
                print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

            if "_" not in guessed_word:
                print("\n" + "="*50)
                print("Congratulations! You've guessed the word correctly!")
                print("="*50)
                break

            if lives <= 0:
                print("\n" + "="*50)
                print("Game Over! You've run out of lives.")
                print(f"The word was: {word}")
                print("="*50)
                break
        
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    hungman_game()