import random


suits = ["hearts" , "diamonds" , "spades" , "clubs"]
values =['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value 
    def __str__(self):
        return f"{self.value}  of  {self.suit}"
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.deck.append(card)  
            

    def __str__(self):
        deck_string = ""
        for card in self.deck:
            deck_string += card.__str__() + "\n"
        return deck_string

    def shuffle(self):
       random.shuffle(self.deck)    


if __name__ == "__main__":
    deck1 = Deck()
    deck1.shuffle()
    print(deck1)
