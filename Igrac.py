from Ploca import Ploca
from Brod import Brod

class Igrac:
    def __init__(self, name, ploca):
        self.name = name
        self.mainPloca = ploca
        self.guessPloca = Ploca([[0 for x in range(8)] for y in range(8)])
        self.brodovi = [Brod(5), Brod(4), Brod(3), Brod(3), Brod(2)]

    def __repr__(self):
        return self.name
