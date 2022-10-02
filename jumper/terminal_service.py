class TerminalService:

    def read_letter(self, prompt):  # reading the letter picked
        letter = input(prompt)
        return letter.lower()

    def write_text(self, text):  # writing text for drawing

        print(text)
