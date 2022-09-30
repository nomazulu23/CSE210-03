#the Jumper code should have the following responsibility:
# 1) draw a line of the parachute if correct letter is picked 
# 2) Remove a line if incorrect letter is picked
# 3) check if there is parachute left with an 0 or no X


class Jumper:
    def __init__(self):
        self._draw_line
        self._remove_line
        self._parachute


def display_parachute(self, tries):
    self._parachute = [ """
                 _____
                /_____\
                \     /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """
                /_____\
                \     /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """          _____\
                \     /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """               \
                \     /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """
                \     /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """               /
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """
                 \   /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """, 
    """
                    /
                   0
                 / | \
                  / \
                ^^^^^^^^^
    """,
    """
                   x
                 / | \
                  / \
                ^^^^^^^^^
    """, 
]

    return self._parachute[tries]