class Brod:
    def __init__(self, length):
        self.length = length
        #   TODO: pratiti unistavanje individualnih brodova
        self.coords = []

    def __repr__(self):
        img = ""
        for _ in range(self.length):
            img += "="

        return img
