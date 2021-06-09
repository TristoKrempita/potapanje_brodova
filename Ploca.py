class Ploca:
    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        final = ""
        for el in [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            final = final + el + " "

        final += "\n"

        for i, row in enumerate(self.arr):
            final += str(i) + " "
            for el in row:
                if el == 0:
                    final += "O" + " "
                elif el == 1:
                    final += "=" + " "
                elif el == 2:
                    final += "X" + " "
                elif el == 3:
                    final += "/" + " "
            final += "\n"

        return final

    def guess_hit(self, x, y):
        if self.arr[x][y] == 1:
            self.arr[x][y] = 2
            return 2
        elif self.arr[x][y] == 0:
            self.arr[x][y] = 3
            return 3
        else:
            return -1

    def set_hit(self, x, y, hit):
        self.arr[x][y] = hit
