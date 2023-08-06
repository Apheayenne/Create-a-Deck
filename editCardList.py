import re
import sqlite3

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def editFile():
    conn = sqlite3.connect("Create-a-deck\Create-a-Deck.db")
    cursor = conn.cursor()

    print("Select a File")
    # subprocess.run(r'explorer /select,"/"')
    # filePath.wait()
    print("Opening that File")

    with open('Create-a-deck\Cards - Raw.txt') as fileCSV:
    # with open(filePath) as fileCSV:
        for line in fileCSV:
            noDeckPrice = line.replace("{noDeck}{noPrice}", "")
            noQty = noDeckPrice.replace('1x ', '')
            noParen = noQty.replace(' (', ';')
            noNumber = re.sub("\) \d+ \[", ") [", noParen)
            noBracket = noNumber.replace(") [" , ";")
            noComma = rreplace(noBracket, ',', ';', 1)
            noEnd = noComma.replace("]","")

            addToDB(noEnd, cursor)
            
    conn.commit

def addToDB(card, cursor):
    cardName, setCode, cycleCat, deckCat = card.strip().split(";")
    sqlInsert = f"""INSERT INTO CARDS (CARD_NAME,SET_CODE,CYCLE_CATEGORY,DECK_CATEGORY) VALUES ("{cardName}","{setCode}","{cycleCat}","{deckCat}");"""
    cursor.execute(sqlInsert)





    