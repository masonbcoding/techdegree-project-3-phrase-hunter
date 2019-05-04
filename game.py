import random

from .phrase import Phrase


class Game:
    guess_limit = 5

    def __init__(self, phrases):
        self.phrases = phrases
        self.game_phrase = Phrase(random.choice(self.phrases))

    def new_game(self):
        self.game_phrase = Phrase(random.choice(self.phrases))

    def start_game(self):
        guesses = []
        incorrect = []

        while True:
            phrase = self.game_phrase.show_phrase()
            print(phrase)
            guess = input("Guess a letter to solve the phrase! ")

            if guess in guesses:
                print("You've already guessed {}. Please try again.".format(guess))
                continue

            try:
                correct = self.game_phrase.check_phrase(guess)

            except ValueError:
                print("Guess must be a single character between a-z or A-Z.")
                continue

            guesses.append(guess)

            if not correct:
                incorrect.append(guess)
                if len(incorrect) >= self.guess_limit:
                    print("Oh, too bad! You've reached the guess limit!")
                    compliance = input("Would you like to play again? [y]es/[n]o: ")

                    if compliance.lower() == 'y':
                        self.new_game()
                        self.start_game()
                        break

                    else:
                        break

            if '_' not in self.game_phrase.show_phrase():
                print("Congratulations! You solved the puzzle!")
                compliance = input("Would you like try another phrase? [y]es or [n]o? ")

                if compliance.lower() == 'y':
                    self.new_game()
                    self.start_game()
                    break

                else:
                    print("Thanks for playing")
                    break

            print("You have {} out of {} guesses remaining.".format(self.guess_limit - len(incorrect),
                                                                    self.guess_limit))
