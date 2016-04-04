from domainobjects.character import Attributes
from domainobjects.character import Character

def main():

    x = Attributes(body=2, agility=7, reaction=5, strength=5, willpower=7, logic=6, intuition=1, charisma=8, edge=9, essence=7)
    print(x.initiative)

    c = Character('Luke', x)
    print(c.attributes.strength)










if __name__ == '__main__':
    main()
