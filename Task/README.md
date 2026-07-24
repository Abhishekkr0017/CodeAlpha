Hangman Game
A simple text-based Hangman game built in Python, where the player guesses a hidden word one letter at a time.

Description
The program randomly selects a word from a predefined list and displays it as a series of underscores. The player guesses letters one at a time. Correct guesses reveal the letter's position(s) in the word; incorrect guesses reduce the player's remaining attempts and add to an ASCII-art hangman drawing. The player wins by guessing the full word before running out of attempts.

Features
5 predefined words (no external files or APIs required)
Maximum of 6 incorrect guesses per game
ASCII-art hangman that updates with each wrong guess
Input validation (rejects empty input, multiple characters, non-letters, and repeated guesses)
Tracks and displays previously guessed letters
Option to play multiple rounds without restarting the program
Concepts Demonstrated
random module — selecting a random word from a list
while loops — controlling the main game loop and replay loop
if-else statements — handling correct/incorrect guesses and validation
Strings — building the masked word display, joining guessed letters
Lists — storing the word bank and guessed letters
How to Run
Make sure Python 3 is installed on your machine.

Save hangman.py to a folder.

Open a terminal in that folder and run:

python hangman.py
Follow the on-screen prompts to guess letters.

Example Gameplay
Welcome to Hangman!
Try to guess the word one letter at a time.
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Guessed letters: None
Incorrect guesses remaining: 6

Guess a letter: e
Good guess! 'e' is in the word.

Word: _ _ e _ _ _
Guessed letters: e
Incorrect guesses remaining: 6
File Structure
hangman.py    # Main game script
README.md     # Project documentation
Possible Future Improvements
Load words from an external file or API for a larger word bank
Add difficulty levels (short vs. long words)
Add a scoring system across multiple rounds
Build a GUI version using Tkinter or a web version using Flask
Author
Submitted as part of an internship assignment.
