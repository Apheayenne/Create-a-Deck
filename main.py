from editCardList import editFile
from CreatetheDeck import creatingDeck


print("Welcome to the Deck Randomizer!")
update = input("Would you like to Update the Deck? Y/N? (Q to quit)\n")

if(update.capitalize() == 'Y'):
    print("Updating Deck!")
    editFile()
elif(update.capitalize() == 'Q'):
    quit()


while True:
    create = input("Would you like to create a new deck? Y or N? (Q to quit)\n")
    if(create.capitalize() == "Y" or create.capitalize() == "N" or create.capitalize() == "Q" ):
        break

if(create.capitalize() == "Y"):
    print("Creating a new Deck!")
    creatingDeck()
    print("Deck Created! Have Fun")
else:
    print("Exiting program!")

quit()