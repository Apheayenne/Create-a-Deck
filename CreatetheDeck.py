import sqlite3
import CreateDecklist as dl

def creatingDeck():
    conn = sqlite3.connect("Create-a-deck/Create-a-Deck.db")
    cursor = conn.cursor()
    Categories = ["Main Deck", "Land", "Mana", "Basic Land", "Commanders"]

    #CMD = 1     # 1 card
    #BASIC = 4   # 4 cards
    #LAND = 3    # 15 Cards
    #MANA = 3    # 15 Cards
    #MAIN = 13   # 65 Cards

    for cat in Categories:
        match cat:
            case "Main Deck":
                count = 13
                chooseMany(cursor, cat, count)
            case "Land":
                count = 3
                chooseMany(cursor, cat, count)
            case "Mana":
                count = 3
                chooseMany(cursor, cat, count)
            case "Basic Land":
                chooseOne(cursor, cat, 4)
            case "Commanders":
                chooseOne(cursor, cat, 1)

    dl.start(finalDeck)

    conn.close
    cursor.close

def chooseOne(cursor, category, count):
    statement = f"""SELECT card_name FROM cards WHERE cards.CYCLE_CATEGORY = '{category}' ORDER BY RANDOM() LIMIT {count};"""
    if category == "COMMANDERS":
        finalDeck.append("\n")
    sqlExecute(cursor, statement)

def chooseMany(cursor, category, count):
    sqlSelectMany = f"""SELECT DISTINCT cycle_category FROM cards WHERE cards.deck_category = '{category}' ORDER BY RANDOM() LIMIT {count};"""
    finding = cursor.execute(sqlSelectMany)
    for item in finding.fetchall():
        for cycle in item:
            findCards(cursor, cycle)

def findCards(cursor, cycle):
    sqlFindCards = f"""SELECT card_name FROM cards WHERE cards.cycle_category = '{cycle}';"""
    sqlExecute(cursor, sqlFindCards)

def sqlExecute(cursor, statement):
    for row in cursor.execute(statement):
        for card in row:
            finalDeck.append(f"{card}\n")
        

finalDeck = []
