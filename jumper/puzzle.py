# the puzzle has the following responsibility
# 1) have a list of secret words
# 2) randomly choose a word
# 3) guess letters of the secret word
# 4) replace underscores with the correct letter, one letter at a time of the secret word
# 5) reject the wrong letter (in jumper for every incorrect letter a line in the parachute is removed)
# 6) number of guesses = length of the secret word & = lines of the parachute
# 6) display the secret word upon completion
# 7) stop guessing if word is completed or guess chances are out


import random


class Puzzle:
    def __init__():
        self._word_list = ["Beetroot", "Cucumber",  "Broccoli", ]
        self._picked_word = " "
        self._guessed_word = ["_"]

    def get_word(self):
        word = random.choice(self._word_list)
        return self._word_list.lower()

    def letter(self):   #randomly picking letters of the secret word
        self._picked_word = random.randint(a, z)
        return self._picked_word.lower()

    def word_completion(self):
        self._guessed_word = ["_"] * len(self._picked_word)
        guessed = False
        guessed_letters = []
        tries = 8

    def guess_process(self,):
        guess_count = 0
        while _is_playing == True:
            if guess_letter == self._picked_word:
                letter = self._guessed_word
            else:
                letter != self._guessed_word
                # remove a line in the parachute

    def end_game(self):
        if self._guessed_word == True:
            print("Game Over")
