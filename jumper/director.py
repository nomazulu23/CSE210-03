# The director is responsible for the following:
# 1) calling files and classes of game
# 2) starting the game
# 3) get input from the user
# 4) displaying the input
# 5) keep progress of the game-
# replace underscores with guessed letters or call the puzzle file to do that
# enable the drawing and removal of lines
# 6) output or displaying results


from terminal_service import TerminalService
from puzzle import Puzzle
from jumper import Jumper


class Director:
    def __init__(self):
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()

    def start_game(self):
        while self._is_playing:
            self._getInputs()
            self._updates()
            self._outputs()

    def _getInputs(self):
        while not guessed and tries > 0:
            guess = input("Guess a letter [a-z]: ").lower
            guess_letter = self._terminal_service.read_letter
            
            if len(guess) == 1 and guess.isalpha():  # guessing the letter
                if guess in guessed_letters:
                    print(guess)

                elif guess not in self._picked_word:
                    print("_")
                    tries -= 1
                    guessed_letters.append(guess)

                else:
                    print(guess)
                    guessed_letters.append(guess)

                    word_as_list = list(self._guessed_word)
                    indices = [i for i, letter in numerate(
                        guess) if guess_letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    self._guessed_word = "".join(word_as_list)
                    if "_" not in self._guessed_word:
                        guess == True

            elif len(guess) == len(self._picked_word) and guess.isalpha():  # guessing the word
                if guess in self._word_list:
                    print(guess)
                elif guess != word:
                    print("_")
                    tries -= 1
                    self._word_list.append(guess)

                else:
                    guessed = True
                    self._guessed_word = self._picked_word
            else:
                print("Not a valid guess.")
            print(display_parachute(tries))
            print(self._guessed_word)

    def _updates(self):
        pass

    def _outputs(self):
        print("Whose ready to Jump!")
        print(display_parachute(tries))
        print(self._guessed_word)
