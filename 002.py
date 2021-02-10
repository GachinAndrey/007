from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def method_1(self):
        print("Одежда:", end=' ')

    @abstractmethod
    def method_2(self):
        print("Параметры:", end=' ')

    @abstractmethod
    def method_3(self):
        print("Расход ткани:", end=' ')


class Coat (Clothes):
    def method_1(self):
        super().method_1()
        print("Пальто")

    def method_2(self):
        super().method_2()
        print("Размер")

    def method_3(self):
        super().method_3()
        return float(self.value) / 6.5 + 0.5


class Suit (Clothes):
    def method_1(self):
        super().method_1()
        print("Костюм")

    def method_2(self):
        super().method_2()
        print("Рост")

    def method_3(self):
        super().method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 50
size_suit = 50

print("\n")
c = Coat(size_coat)
c.method_1()
c.method_2()
print("%.2f" % c.method_3())


print("\n")
s = Suit(size_suit)
s.method_1()
s.method_2()
print("%.2f" % s.method_3())


t = Total(size_coat, size_suit)
print("\nОбщий расход ткани: %.2f" % t.sum())


