# The director is responsible for the following:
# 1) calling files and classes of game
# 2) starting the game
# 3) get input from the user
# 4) displaying the input
# 5) keep progress of the game-
# replace underscores with guessed letters or call the puzzle file to do that
# enable the drawing and removal of lines
# 6) output or displaying results


from puzzle import Puzzle


class Director:
    def __init__(self):
        self._puzzle = Puzzle()
        self._is_playing = True

    def start_game(self):
        while self._is_playing:
            self._getInputs()
            self._updates()
            self._outputs()

    def _getInputs(self):
        self._puzzle.letter()
            

    def _updates(self):
        self._puzzle.end_game()
        if self._puzzle._validate == 1:
            self._is_playing = False
        elif self._puzzle._validate == 2:
            self._is_playing = False

    def _outputs(self):
        print("Whose ready to Jump!")
