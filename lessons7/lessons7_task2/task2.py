from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def price(self):
        pass

    @property
    def __add__(self, other):
        return str(f'Общая площадь ткани {self.param + other.param}')

class Coat(Clothes):

    @property
    def price(self):
        return self.param / 6.5 + 0.5

    def __str__(self):
        return f'S of coat {self.param}'

class Jacket(Clothes):

    @property
    def price(self):
        return self.param * 2 + 0.3

    def __str__(self):
        return f'S of jacket {self.param}'

clother1 = Coat(32)
clother2 = Jacket(66)
print(clother1)
print(clother2)
print(clother1.param + clother2.param)