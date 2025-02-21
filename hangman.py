word_list = ['franky', 'mwendwa', 'mutisaa']

import random
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

lives = end_of_game

guessed_letter = input("Please guess a letter!").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guessed_letter:
        display[position] = letter
print(display)