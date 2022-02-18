class Stationery:

     def __init__(self, title):
         self.title = title

     def draw(self):
         print('Run drawing')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'You start drawing with {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'You start drawing with {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'You start drawing with {self.title}')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркет')
print(pen.draw())
print(pencil.draw())
print(handle.draw())