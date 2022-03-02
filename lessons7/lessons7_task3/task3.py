
class Cell:

    def __init__(self, cells):
        self.cells = int(cells)
        self.simbol = '*'

    def __str__(self):
        return str(f'Количесвто ячеек - {self.cells}')

    def __add__(self, other):
        return Cell(abs(self.cells + other.cells))

    def __sub__(self, other):
        return Cell(abs(self.cells - other.cells))

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, count):
        i = self.cells
        while i > 0:
            for k in range(1, count + 1):
                print(self.simbol, end = '')
                i -= 1
                if i <= 0:
                    break
            print('\n', end= '')

cell_1 = Cell(3)
cell_2 = Cell(9)


print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)

cell_1.make_order(4)
cell_2.make_order(2)