class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def __iter__(self):
        yield from self.phrase


    def __eq__(self, other):
        if self == other:
            return True


    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print("{}".format(letter), end=" ")
            elif letter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print("\n")


    def check_letter(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False
            print("You, chose poorly... Please try again.")
            
            
    def check_complete(self, guesses):
        guessed = set(guesses)
        required = set()
        for letter in self.phrase:
            required.add(letter)
        required.remove(' ')
        if not len(required - guessed):
            return True
        return False
