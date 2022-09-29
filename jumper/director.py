from jumper.terminal_service import terminal_service
from jumper.puzzle import Puzzle
from jumper.jumper import Jumper


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
        guess = input("Guess a letter [a-z]:")
        guess_letter = self._terminal_service.read_letter

    def _updates(self):
        pass

    def _outputs(self):
        pass
