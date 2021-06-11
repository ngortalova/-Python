import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "yellow"
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = "green"
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "red"


a = TrafficLight()
a.running()
b = TrafficLight()
b.running()
