class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Вычитание: {sub}' if sub > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cells_1 = Cell(12)
cells_2 = Cell(15)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_1 * cells_2)
print(cells_1 / cells_2)
print(cells_1.make_order(5))
print(cells_2.make_order(5))
