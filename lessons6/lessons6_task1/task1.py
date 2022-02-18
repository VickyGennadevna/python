from time import sleep

class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__colors[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(4)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()