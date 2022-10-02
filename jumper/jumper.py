
#the Jumper code should have the following responsibility:
# 1) draw a line of the parachute if correct letter is picked 
# 2) Remove a line if incorrect letter is picked
# 3) check if there is parachute left with an 0 or no X


class Jumper:
    def __init__(self):
      self._parachute = [ "_____", "/_____\\", "\     /", "\   /"]
      self._person = [ "0 ", "/ | \\", " / \\ ", "^^^^^^^"]


    def display_parachute(self):
        print(self._parachute)
          

    def display_person(self):
        print(self._person)

    def cut_line(self):
        self._parachute.pop(0)
