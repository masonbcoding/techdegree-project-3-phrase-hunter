import re


class Character:
    def __init__(self, char):
        if len(char) != 1:
            raise ValueError("You can only choose a single character.")

        self.instance = char

        if self.instance == ' ':
            self.attempt = True

        else:
            self.attempt = False

    def check(self, guess):
        Character.character_check(guess)

        if guess.lower() == self.instance:
        	self.attempt = True
        	return True

        elif guess.upper() == self.instance:
            self.attempt = True
            return True

        else:
            return False

    def show(self):
        if self.instance == ' ':
            return self.instance

        if self.attempt:
            return self.instance

        else:
            return '_'

    @staticmethod
    def character_check(guess):
        pattern = r'^[a-zA-Z]$'
        prog = re.compile(pattern)
        if not prog.match(guess):
            raise ValueError("Only upper- or lower-cased alphabet characters allowed, i.e. a-z, A-Z")
