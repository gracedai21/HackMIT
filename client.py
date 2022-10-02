from flashcard import Flashcard

print()
numCards = int(input("How many flashcards are you making? "))

flashCardList = []
for i in range(numCards):
    front = input("Front: ")
    mid = input("Mid: ")
    back = input("Back: ")
    print()
    
    flashCardList += [Flashcard(front, mid, back)]

for card in flashCardList:
    side = input("Which side do you want to see? (f, m, b): ")
    print()
    
    if side == "f":
        print(card.front)
        repeat1 = True

        while(repeat1):
            m = input("m?: ")
            if m == card.middle:
                repeat1 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()
        
        repeat2 = True
        while(repeat2):
            b = input("b?: ")
            if b == card.back:
                repeat2 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()
    
    elif side == "m":
        print(card.middle)
        repeat1 = True

        while(repeat1):
            f = input("f?: ")
            if f == card.front:
                repeat1 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()
        
        repeat2 = True
        while(repeat2):
            b = input("b?: ")
            if b == card.back:
                repeat2 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()
    
    elif side == "b":
        print(card.back)
        repeat1 = True

        while(repeat1):
            f = input("f?: ")
            if f == card.front:
                repeat1 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()
        
        repeat2 = True
        while(repeat2):
            m = input("m?: ")
            if m == card.middle:
                repeat2 = False
                print("Correct!")
                print()
            else:
                print("Incorrect. Try Again.")
                print()

            

#def printSpecific():
 #   cardIndex = int(input("Which flashcard do you want to see? "))
  #  print(flashCardList[cardIndex - 1])