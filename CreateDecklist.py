from xml.dom import minidom as dom
import datetime as date
from operator import itemgetter


def start(deckList):

    fileName = date.date.today()

    doc = dom.Document()
    top = doc.createElement("cockatrice_deck")
    top.setAttribute('version', "1")
    doc.appendChild(top)

    mainZone = doc.createElement("zone")
    mainZone.setAttribute("name", "main")
    top.appendChild(mainZone)

    i = 1
    for card in deckList:
        attribute = ["number", "1", "name", card]
        if(i != 100):
            addElement(doc, mainZone, "card", attribute)
            i += 1
        else:
            sideZone = doc.createElement("zone")
            sideZone.setAttribute("name", "side")
            top.appendChild(sideZone)
            addElement(doc, sideZone, "card", attribute)

    doc.writexml(open(f'C://Users//howan//Desktop//CockatricePortable//data//decks//{fileName}.cod','w'),"\t","\t", "\n")



def addElement(doc, parent, elementName, attributeList):
    tempElement = doc.createElement(elementName)

    qty, qtyValue, card, cardValue = itemgetter(0,1,2,3)(attributeList)
    tempElement.setAttribute(qty, qtyValue)
    tempElement.setAttribute(card, cardValue.strip())
    parent.appendChild(tempElement)
    
