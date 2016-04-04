class Character:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes):
        self.__validateattributes(attributes)
        self.__attributes = attributes

    def __validateattributes(self, attributes):
        if not isinstance(attributes, Attributes):
            raise TypeError('Attributes Property Not Correct Type')

class Attributes:
    def __init__(self, body, agility, reaction, strength, willpower, logic, intuition, charisma, edge, essence):
        self.body = body
        self.agility = agility
        self.reaction = reaction
        self.strength = strength
        self.willpower = willpower
        self.logic = logic
        self.intuition = intuition
        self.charisma = charisma
        self.edge = edge
        self.essence = essence

    @property
    def body(self):
        return self.__body

    @property
    def agility(self):
        return self.__agility

    @property
    def reaction(self):
        return self.__reaction

    @property
    def reaction(self):
        return self.__reaction

    @property
    def strength(self):
        return self.__strength

    @property
    def willpower(self):
        return self.__willpower

    @property
    def logic(self):
        return self.__logic

    @property
    def intuition(self):
        return self.__intuition

    @property
    def charisma(self):
        return self.__charisma

    @property
    def edge(self):
        return self.__edge

    @property
    def essence(self):
        return self.__essence

    @property
    def initiative(self):
        return self.__reaction + self.__intuition

    @body.setter
    def body(self, body):
        self.__validateattribute(body);
        self.__body = body

    @agility.setter
    def agility(self, agility):
        self.__validateattribute(agility);
        self.__agility = agility

    @agility.setter
    def reaction(self, reaction):
        self.__validateattribute(reaction);
        self.__reaction = reaction

    @strength.setter
    def strength(self, strength):
        self.__validateattribute(strength);
        self.__strength = strength

    @willpower.setter
    def willpower(self, willpower):
        self.__validateattribute(willpower);
        self.__willpower = willpower

    @logic.setter
    def logic(self, logic):
        self.__validateattribute(logic);
        self.__logic = logic

    @intuition.setter
    def intuition(self, intuition):
        self.__validateattribute(intuition);
        self.__intuition = intuition

    @charisma.setter
    def charisma(self, charisma):
        self.__validateattribute(charisma);
        self.__charisma = charisma

    @edge.setter
    def edge(self, edge):
        self.__validateattribute(edge);
        self.__edge = edge

    @essence.setter
    def essence(self, essence):
        self.__validateattribute(essence);
        self.__essence = essence

    def __validateattribute(self, attributevalue):
        if isinstance(attributevalue, int):
            if attributevalue < 1 or attributevalue > 50:
                raise AttributeError('Attribute Values Must be Between 1 and 50')
        else:
            raise TypeError('Attribute Values Should be Integers')
