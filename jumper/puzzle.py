# the puzzle has the following responsibility

# 1) have a list of secret words

# 2) randomly choose a word

# 3) guess letters of the secret word

# 4) replace underscores with the correct letter, one letter at a time of the secret word

# 5) reject the wrong letter (in jumper for every incorrect letter a line in the parachute is removed)

# 6) number of guesses = length of the secret word & = lines of the parachute

# 6) display the secret word upon completion

# 7) stop guessing if word is completed or guess chances are out


from terminal_service import TerminalService

from jumper import Jumper
import random



class Puzzle:

    def __init__(self):

        self.terminal_service = TerminalService()
        self._jumper = Jumper()
        self._word_list = ["Beetroot", "Cucumber",  "Broccoli", ]
        self._picked_word = ""
        self._word = []
        self._blank_word = []
        self._guessed_letters = []
        self._validate = 0

    def get_word(self):
        self._picked_word = random.choice(self._word_list)
        return self._picked_word.lower()

    def fill_list(self):
        for i in self._picked_word:
            self._word.append(i)
            self._blank_word.append("_")

    def letter(self):   #randomly picking letters of the secret word

        guess = self.terminal_service.read_letter("Guess a letter [a-z]: ")
        

        if len(guess) == 1 and guess.isalpha():  # guessing the letter

            if guess in self._word:

                index = self._word.index("guess")

                self._blank_word[index] = self._word[index]

                print("".join(self._blank_word))

                self._jumper.display_parachute()

                self._jumper.display_person()


            elif guess not in self._word:

                if len(self._jumper) > 0:

                    self._jumper.cut_line()
                    self._guessed_letters.append(guess)

                    self._jumper.display_parachute()

                    self._jumper.display_person()

        else:

            print("Not a valid guess.")

            self._jumper.display_parachute()

            self._jumper.display_person()
            print(self._guessed_word)


    def word_completion(self):

        self._guessed_word = ["_"] * len(self._picked_word)

        guessed = False

        guessed_letters = []

        tries = 8


    def end_game(self):

        if self._word == self._blank_word:

            print("You win! Congrats!")
            self._validate = 1

        elif len(self._jumper._parachute) == 0:

            print("You lose! Game Over")
            self._validate = 2

