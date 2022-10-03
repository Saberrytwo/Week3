# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s): # Milestone 2 function
        s = s.lower()
        if s in wordList:
            gw.show_message("This is a valid guess")
        else:
            gw.show_message("Not in Word List")
    wordList = set(FIVE_LETTER_WORDS)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)

    for i, letter in enumerate(random_word):
        gw.set_square_letter(0, i, letter)

if __name__ == "__main__":
    wordle()
