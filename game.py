from phrase import Phrase
import random


class Game:
    def create_phrases(self):
        phrases = [Phrase("Misfit Love"), Phrase("Battery Acid"), Phrase("God is in the Radio"), Phrase("Go With the Flow"), Phrase("Make it wit Chu")]
        return phrases


    def get_random_phrase(self):
        return random.choice(self.phrases)


    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []


    def welcome(self):
        print(" "*9+"_"*47+"""\n
        === GET READY TO PLAY PH-PH-PH-PHRASE HUNTER ===
        """+"_"*48, "\nGET READY TO CHOOSE YOUR LETTER AT THE PROMPT. YOU HAVE 5 GUESSES. LET'S GO !!!\n")


    def get_guess(self):
        while True:
            user_guess = (input("Choose your letter: ")).lower()
            if not user_guess.isalpha():
                print("You may only choose alphabet characters, i.e. a-z, A-Z. Please try again.")
            elif len(user_guess) != 1:
                print("Sorry! You're only allowed one choice at a time. Please select a letter.")
            else:
                return user_guess
            
    def game_over(self):
        print('Would you like to play again?')
        answers = ['y', 'n']
        answer = input('y/n: ').lower()
        
        while answer not in answers:
            print("Please enter y or n...")
            answer = input('y/n: ').lower()

        while answer == 'y':
            game = Game()
            game.start()
            print('Would you like to play again?')
            answer = input('y/n: ').lower()
            while answer not in answers:
                print("Please enter y or n...")
                answer = input('y/n: ').lower()

        print("\nWE HOPE YOU ENJOYED PLAYING PHRASE HUNTER! PLEASE COME BACK AND CHECK FOR NEW PHRASES AND CHALLENGES! ")


    def start(self):
        self.welcome()
        self.active_phrase.display(self.guesses)

        while self.missed != 5:
            print("You have currently used {} guesses.\n".format(self.missed))
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if self.active_phrase.check_letter(user_guess):
                print("CORRECT!\n")
                self.active_phrase.display(self.guesses)
                if self.active_phrase.check_complete(self.guesses):
                    print("CONGRATULATIONS! YOU UNCOVERED THE PHRASE!\n")
                    break
            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1
                print("\nSORRY! THAT GUESS WAS INCORRECT. PLEASE TRY AGAIN.\n")

        if self.missed == 5:
            print("Sorry, you've used up all your choices... ")
