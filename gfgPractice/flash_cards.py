import random

class flashCards:
    def __init__(self , question , meaning):
        self.question = question
        self.answer = answer

    def quiz(self):
        pass

    def __str__(self):
        return "qusetion: " + self.question + "\nanswer: " + self.answer    

if __name__ == "__main__":
    flash_cards = []
    flag = 1

    while flag:
        question = input("enter question you want to enter \n")
        answer = input("enter answer of question \n")
        flashcard = flashCards(question , answer)
        flash_cards.append(flashcard)

        flag = int(input("enter 0 to exit and 1 to continue"))

    flag = 1

    print("quizz for flash")

    while flag:
        flashcard = random.choice(flash_cards)
        print("flash card question:")
        print(flashcard.question)
        answer = input("enter answer to above question: ")
        if flashcard.answer == answer:
            print("correct answer")
        else:
            print("incorrect answer")

        flag = input("enter 0 to exit or 1 to continue quiz ")        
        