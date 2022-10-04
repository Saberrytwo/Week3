# File: Wordle.py
# Test, can Solomon finally edit??

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():

    target_word = random.choice(FIVE_LETTER_WORDS)
    print(target_word)

    def enter_action(s): # Milestone 2 function
        s = s.lower()
        if s in wordList:
            gw.show_message("This is a valid guess")
            color_letters(target_word, s, 0)
        else:
            gw.show_message("Not in Word List")
    wordList = set(FIVE_LETTER_WORDS)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    def color_letters(target_word, guess_word, current_row):

        target_buffer = target_word
        guess_buffer = guess_word

        for index, letter in enumerate(target_word):
            if target_word[index] == guess_word[index]:
                gw.set_square_color(current_row, index, CORRECT_COLOR)
                target_buffer = target_buffer[:index] + "0" + target_buffer[index+1:]
                guess_buffer = guess_buffer[:index] + "0" + guess_buffer[index+1:]
        
        for index, letter in enumerate(guess_buffer):
            if guess_buffer[index] == "0":
                continue
            location = target_buffer.find(guess_buffer[index])
            if location != -1:
                gw.set_square_color(current_row, index, PRESENT_COLOR)
                target_buffer = target_buffer[:location] + "0" + target_buffer[location+1:]


if __name__ == "__main__":
    wordle()
