class Quiz:

    def __init__(self, deck, property_1, property_2):
        self.deck = deck
        self.property_1 = property_1
        self.property_2 = property_2
    
    def start(self):

        import random
        random.shuffle(self.deck)

        amount = len(self.deck)

        BLUE = "\033[94m"
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"

        wrong = []

        for index, card in enumerate(self.deck):

            answer = input(f"{index+1}/{amount} | {self.property_1.capitalize()}: " + BLUE + card.getSide(self.property_1) + RESET + f". {self.property_2.capitalize()}: ")

            if not answer:
                print("The answer is " + BLUE + card.getSide(self.property_2) + RESET + ".")
                wrong.append(card)
                continue

            if answer.lower() == card.getSide(self.property_2).lower():
                print(GREEN + "Correct! " + RESET)
            else:
                print(RED + "Wrong! " + RESET + "The answer is " + BLUE + card.getSide(self.property_2) + RESET + ".")
                wrong.append(card)
        
        if len(wrong) > 0:
            print(f"Got {len(wrong)} {'cards' if len(wrong) > 1 else 'card'} wrong.")
            answer = input("Do you want to try the cards you got wrong again? (y/N) ")

            if answer.lower() == "y":
                print("\033c" + f"Starting over with the {'cards' if len(wrong) > 1 else 'card'} you got wrong.\n")
                self.deck = wrong
                self.start()
            else:
                print("Thanks for playing!")

        else:
            print("\nSolved all cards! Thanks for playing!")
