from .character import Character


class Phrase:

    def __init__(self, phrase):
        try:
            self.phrase = [Character(c) for c in phrase]
        except Exception:
            print("Oh no! We're experiencing an error. Please try again. Enter an alphabet character, i.e. a-z, A-Z")
            exit(1)


    def show_phrase(self):
        return ' '.join([c.show() for c in self.phrase])


    def check_phrase(self, guess):
        correct = False
        for c in self.phrase:
            if c.check_phrase(guess):
                correct = True
        return correct
