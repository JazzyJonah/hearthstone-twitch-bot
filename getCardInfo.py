import requests
import re


def getCardInfo(name):
    cleanName = "".join(filter(str.isalnum, name))
    cards = requests.get("https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json").json()
    
    allCardTypes = []
    for card in cards:
        try:
            if card["type"] not in allCardTypes:
                allCardTypes.append(card["type"])
                allCardTypes.append(card["name"])
        except:
            # print(card, "error")
            pass
    print(allCardTypes)

    # first try exact search
    for card in cards:
        # if 'battlegroundsHero' in card:
        #     continue
        cleanCardName = "".join(filter(str.isalnum, card["name"]))
        if cleanName.lower() == cleanCardName.lower():
            # return card
            print(card)
            return getCardMessage(card)
    
    # then try partial search
    for card in cards:
        if 'battlegroundsHero' in card:
            continue
        cleanCardName = "".join(filter(str.isalnum, card["name"]))
        if cleanName.lower() in cleanCardName.lower():
            print(card)
            return getCardMessage(card)
        
def getCardMessage(card):
    try:
        cardText = cleanCardText(card["text"]) if "text" in card else ""
        if 'classes' in card:
            cardClass = "/".join(card["classes"]).lower()
        else:
            cardClass = card["cardClass"].lower()
        if card["type"] == "SPELL":
            return f'{card["name"]} | {card["cost"]} mana {cardClass} {card["rarity"].lower()} spell | {cardText}'
        elif card["type"] == "MINION":
            return f'{card["name"]} | {card["cost"]} mana {cardClass} {card["rarity"].lower()} minion | {card["attack"]}/{card["health"]} | {cardText}'
        elif card["type"] == "WEAPON":
            return f'{card["name"]} | {card["cost"]} mana {cardClass} {card["rarity"].lower()} weapon | {card["attack"]}/{card["durability"]} | {cardText}'
        elif card["type"] == "HERO":
            return f'{card["name"]} | {card["cost"]} mana {cardClass} {card["rarity"].lower()} hero card | {card["armor"]} armor | {cardText}'
        elif card["type"] == "LOCATION":
            return f'{card["name"]} | {card["cost"]} mana {cardClass} {card["rarity"].lower()} location | {card["health"]} durability | {cardText}'
        else:
            return 'Achivement unlocked: how did we get here?'
    except:
        return "Achievement unlocked: how did we get here?"
        
# write a function that removes everything between [] and <> (inclusive) and removes any \ and a singular character after it

def cleanCardText(text):
    print(text)
    # Remove HTML tags
    cleaned_text = re.sub(r'<.*?>', '', text)
    # Remove special characters
    cleaned_text = re.sub(r'\\n', ' ', cleaned_text)
    cleaned_text = re.sub(r'\[x\]', '', cleaned_text)
    cleaned_text = re.sub(r'\xa0', ' ', cleaned_text)
    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

print(getCardInfo("crimson expanse"))