Create-a-Deck

This is a personal project to create a deck based off of as many different cycles in Magic the Gathering.

A cycle is a group of cards, usually 5 or 10, that are somehow related. Some examples would be:
    
    • "Shock Lands": A group of 10 lands (5 ally and 5 enemy colors) that deal 2 damage to play the land untapped
    • "Archetypes": A group of 5 creatures whose names are 'Archetype of [word]'. Each creature gives all your creatures a keyword, 
    and creatures your opponents have lose and cannot gain said keyword.
    • "Spirit Avatar": 2 Groups of 5 cards from Shadowmoor (Ally) and Eventide (Enemy) whose Mana cost is 5 hybrid colors 
    and card type is Spirit Avatar

You can see full Decklist on my Archidekt account: https://www.archidekt.com/decks/3822401/cycles_deck. Feel free to suggest any cycle you think should be in the deck.

Changelog

08/06/2023:
Adding cards to Database
    
    • Takes CSV list of cards from Archidekt
    • Edits CSV to be only what this program can use
    • Adds cards to database 

Creating Deck
    
    • Deck is split into 5 categories: 
        • Commanders, 1: Group of 5, 5-color commanders. No real cycle here, just a wide range of options.
        • Basic Land, 1: 1 land will be removed in place of the commander
        • Land, 3: Land cycles
        • Mana, 3: Non-Land mana production
        • Main Deck, 13: All other cards that will be used: instants, sorceries, creatures, planeswalkers, etc. 
    • Each group will choose a number of cycles (see above next to categories) to be randomly chosen to be put into the deck.
    • Once Decklist is chosen, the program will create an xml document of the decklist. 
    • Can only use with Cockatrice. 
