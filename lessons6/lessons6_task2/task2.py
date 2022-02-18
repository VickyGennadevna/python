class Road:
    _length = None
    _width = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self):
        self.weight = 25
        self.numbers = 5
        intake = self._length * self._width * self.weight * self.numbers
        print(f'need {intake}')

road_in_city = Road(20, 5000)
road_in_city.asphalt_mass()