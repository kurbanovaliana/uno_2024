class Card:
    colors = ('red','green','blue','yellow')
    numbers = list(range(10))+ list (range(1, 10))
    dcolors = {color[0]: color for color in colors}
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number
    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    def __repr__(self):
        letter=self.color[0]
        return f'{letter}{self.number}'

@classmethod

def load(cls, text: str):
    letter = text[0]
    number = text[1]
    color = cls.dcolors[letter]
    card = Card(color, int(number))
    return card

def playable(self, other):

