# Python Library hangman Game
A command-line Hangman game focused on guessing popular python libraries. Test your knowledge of python packages while having fun with this classic-word guessing game!

##  Features
🎯 Python-Themed: All words are popular Python libraries/packages
💡 Intelligent Clues: Get helpful hints about the library after wrong guesses
📊 Game Statistics: Track guessed letters, remaining lives, and progress
🔄 Replay System: Play multiple rounds with different words
🎮 User-Friendly: Clean interface with input validation
📝 Learning Tool: Discover new Python libraries while playing

## Game Rules
  - Objective: Guess the hidden Python library name letter by letter
  - Lives: You start with 6 lives
  - Clues: Receive hints about the library after wrong guesses
  - Input: Enter one letter at a time
  - Win Condition: Guess all letters before running out of lives
  - Loss Condition: Run out of lives (6 wrong guesses)

## How to Play

### Prerequisities
  python 3x installed on your system

1.Make sure you have Python 3 installed.
2.Open a terminal or command prompt.
3.Navigate to the folder where hangman.py is located:
```bash
cd CodeAlpha-Python-Internship/Hangman
```
Run the script:
```bash
 python hangman.py
```
## Game Commands

| Command |	Action|
|---------|--------|
|Single letter	 |  Guess that letter|
|quit |  Exit the game | 
|yes / no	| Play again or exit|

## 📊 Game Features in Detail

### 1. Word Selection
Randomly selects from popular Python libraries
Includes libraries like: NumPy, Pandas, matplotlib, seaborn, sklearn, etc..

### 2. Clue System
Initial hint: Word length only
Additional clues provided after wrong guesses
Clues describe the library's purpose

### 3. Progress Display
```bash
Word: _ _ _ _ _ _            (NumPy example)
Guessed letters: a, e, n, p
Lives remaining: 4
```

### 4. Input Validation
Accepts only single letters
Case-insensitive (A = a)
Prevents duplicate guesses
Validates alphabetical characters only

#### 🏗️ Code Structure
```bash
python
hangman_game()           # Main game function
├── python_libraries     # Dictionary of words and clues
├── Game initialization  # Setup variables and display
├── Game loop           # Main gameplay logic
│   ├── Input handling  # Validate and process guesses
│   ├── Letter checking # Check if guess is correct
│   ├── Clue system     # Provide hints on wrong guesses
│   ├── Win/lose check  # Determine game outcome
│   └── Display update  # Show current game state
└── Replay system       # Ask to play again
```

#### 📝 Example Game Session
```markdown
==================================================
Welcome to Hangman Game!
==================================================
Guess the word letter by letter
This word is one of the famous Python libraries
Length of word: 6
Word: _ _ _ _ _ _
Lives remaining: 6

Enter a letter: a
Good guess! 'a' is in the word.
Word: _ a _ _ _ _
Guessed letters: a

Enter a letter: e
Wrong guess! 'e' is not in the word.
Lives remaining: 5
Word: _ a _ _ _ _
Guessed letters: a, e
... (game continues)
```

## Future Improvement
- Add more Libraries
- Score tracking and high score
- Difficulty levels
- Timer mode

## project Info
Internship: CodeAlpha – Python Programming
Task: create a simple Hangman Game
Developer: Bhoomika D A
