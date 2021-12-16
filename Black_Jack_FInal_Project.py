import random
# __________________________________________________________________________________________
class Deck:

    # constructor
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.kinds = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self.card = ""
        self.deck = []
        self.shuffleddeck = []
        self.value = 0

    # get deck
    def get_deck(self):
        for suit in self.suits:
            for kind in self.kinds:
                self.deck.append(kind + " of " + suit)
        return self.deck

    # shuffles deck
    def shuffle_and_get_deck(self):
        self.shuffleddeck = random.sample(self.deck, len(self.deck))
        return self.shuffleddeck

    # gets card from deck
    def get_card(self):
        self.card = self.shuffleddeck.pop()
        return self.card
# __________________________________________________________________________________________

class Player:
    
    # initializing deck
    deck = Deck()
    deck.get_deck()
    deck.shuffle_and_get_deck()

    # constructor
    def __init__(self):
        self.card = ""
        self.hand = []
        self.value = 0
        self.currSum = 0
        self.numkinds = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10}
        self.ace_counter = 0

    # gets 2 cards
    def hit2times(self):
        self.card = self.deck.get_card()
        self.hand.append(self.card)
        self.card = self.deck.get_card()
        self.hand.append(self.card)

    # get 1 card
    def hit(self):
        # note: Reminder, using a class type inside a class "self.deck.get_card()"
        self.card = self.deck.get_card()
        self.hand.append(self.card)

    # get hand
    def get_hand(self):
        return self.hand

    # get total
    def get_total(self):
        self.ace_counter = 0
        self.currSum = 0
        for i, card in enumerate(self.hand):
            if card.split()[0] == 'Jack' or card.split()[0] == 'Queen' or card.split()[0] == 'King':
                self.value = 10
                self.currSum += self.value
            if card.split()[0] in self.numkinds:
                self.value = self.numkinds[card.split()[0]]
                self.currSum += self.value
            # dealing with Aces 1 or 11
            if card.split()[0] == 'Ace' and self.currSum > 10:
                self.value = 1
                self.currSum += self.value
            if card.split()[0] == 'Ace' and self.currSum <= 10:
                self.value = 11
                self.currSum += self.value
                self.ace_counter += 1
        # accounts for ace(s) = 11 and currSum greater than 21, then player would want ace to equal 1
        if self.ace_counter == 1 and self.currSum > 21:
            self.currSum -= 10
        elif self.ace_counter == 2 and self.currSum > 21:
            self.currSum -= 20
        elif self.ace_counter == 3 and self.currSum > 21:
            self.currSum -= 30
        elif self.ace_counter == 4 and self.currSum > 21:
            self.currSum -= 40
        # return statement
        return self.currSum

#__________________________________________________________________________________________
# BlackJack class inherits from Player class
class BlackJack:

    # constructor
    def __init__(self):
        self.win = False
        self.play = 'y'
        self.user_choice = 'h'
        self.turn = 1
        # creating instance dealer and player
        self.dealer = Player()
        self.player = Player()

    # reset 
    def reset(self):
        self.play = 'y'
        self.user_choice = 'h'
        self.turn = 1
        self.dealer = Player()
        self.player = Player()

    # executes menu
    def execute(self):
        while True:
            print("WELCOME TO BLACKJACK!")
            print("Rules:")
            print("1. The goal is to hit 21 or get as close as possible without busting(over 21) while beating the dealer.")
            print("2. If you choose not to hit(stand) the dealer can hit till 17 to attempt to beat your total.")
            print("3. Kings, Queens, and Jacks are worth are worth 10 points.")
            print("4. Aces are 1 or 11 in your favor.")
            print()
            # creating instance object
            newDeck = Deck()
            # getting cards for deck
            newDeck.get_deck()
            # shuffling deck
            newDeck.shuffle_and_get_deck()
            # dealer and player get 2 cards each at the start
            self.dealer.hit2times()
            self.player.hit2times()
            # output dealer and player total
            print("Dealer hand: ", self.dealer.get_hand())
            print("Dealer total: ", self.dealer.get_total())
            print("Player hand: ", self.player.get_hand())
            print("Player total: ", self.player.get_total())
            print()
            if self.player.currSum != 21:
                # input validation
                allowed_choices_menu = ['s', 'h']
                menu()
                self.user_choice = input()
                while self.user_choice not in allowed_choices_menu:
                    print()
                    print("Sorry, I didn't understand your input.")
                    menu()
                    self.user_choice = input()
            while True:
                # loop for player stand, player hit
                if self.player.currSum != 21:
                    while self.user_choice == 'h':
                        self.player.hit()
                        print("Player hand: ", self.player.get_hand())
                        print("Player total: ", self.player.get_total())
                        print()
                        # will exit loop if player hits 21 or bust
                        if self.player.currSum >= 21:
                            break
                        menu()
                        self.user_choice = input()
                        # input validation
                        while self.user_choice not in allowed_choices_menu:
                            print()
                            print("Sorry, I didn't understand your input.")
                            menu()
                            self.user_choice = input()
                    if self.player.currSum < 21:
                        # dealer will hit if less than 17 and dealer sum less than player sum
                        while self.dealer.currSum < 17 and (self.dealer.currSum < self.player.currSum):
                            print()
                            print("Rebuttal, dealer hits till 17.")
                            self.dealer.hit()
                            print("Dealer hand: ", self.dealer.get_hand())
                            print("Dealer total: ", self.dealer.get_total())
                            print()
                # test if player won per iteration
                if self.dealer.currSum > 21:
                    print("Dealer Bust! You Win!\n")
                    break
                if self.player.currSum > 21:
                    print("Bust! You lose.\n")
                    break
                if self.dealer.currSum == self.player.currSum:
                    print("Push! No one wins.\n")
                    break
                if self.player.currSum == 21:
                    print("BlackJack! You win!\n")
                    break
                if self.dealer.currSum > self.player.currSum:
                    print("Dealer has a higher total. You lose.\n")
                    break
                if self.dealer.currSum < self.player.currSum:
                    print("Player has a higher total. You win!\n")
                    break

            # rerun loop
            allowed_choices = ['y', 'n']
            self.play = input("Do you want to play again? (y/n): ")
            # input validation
            while self.play not in allowed_choices:
                print("Sorry, I didn't understand your input.")
                self.play = input("Do you want to play again? (y/n): ")
            print()
            if self.play == 'n':
                print("Goodbye.")
                print()
                break
            elif self.play == 'y':
                self.reset()
                print("____________NEW GAME____________")
                print()
                continue

# menu
def menu():
    print("CHOOSE AN OPTION: ")
    print("1. stand     -s: ")
    print("2. hit       -h: ")
    print("Enter here:", end=" ")

#-------- MAIN --------------
if __name__ == "__main__":
    newgame = BlackJack()
    newgame.execute()





# test bench _____________
#
#     testbob = Player()
    # below is equivalent to 2 hits
    # print(testbob.hit())
    # print(testbob.hit())
    # print(testbob.hit2times())
    #
    # testbob.print_total()




