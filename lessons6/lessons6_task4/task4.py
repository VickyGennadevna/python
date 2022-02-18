class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
    def go(self):
        return 'The car run'
    def stop(self):
        return 'The car stop'
    def turn(self):
        return 'The car turned to'
    def show_speed(self):
        return f'Speed is {self.speed}'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed is {self.speed}')
        if self.speed > 60:
            print('Speed of the car is higher then allow')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class Workcar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of the car is {self.speed}')
        if self.speed > 40:
            print('Speed of the car is higher then allow')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

bmw = TownCar(140, 'black', 'BMW', True)
audi = SportCar(180, 'grey', 'AUDI', False)
mazda = Workcar(50, 'white', 'MAZDA', False)
ford = PoliceCar(100, 'blue', 'FORD', False)
print(bmw.go())
print(audi.show_speed())
print(mazda.show_speed())
print(ford.stop())
