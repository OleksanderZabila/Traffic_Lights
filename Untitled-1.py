import time
class TrafficLightControl:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.light_red = Red()
        self.light_yellow = Yellow()
        self.light_green = Green()

    def run(self):
        self.traffic_light.changelight(self.light_red)

    def stop(self):
        self.traffic_light.changelight("stop")

class TrafficLight:
    def __init__(self):
        self.light = None

    def changelight(self, light):
        self.light = light

class Light:
    def GetColor(self):
        pass

class Red(Light):
    def GetColor(self):
        return "Red"

class Green(Light):
    def GetColor(self):
        return "Green"

class Yellow(Light):
    def GetColor(self):
        return "Yellow"

class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def run(Light):
        while True:
            print(Green) 
            time.sleep(5)
            print(Yellow) 
            time.sleep(2)
            print(Red) 
            time.sleep(5)

# создаем объект светофора и запускаем его
traffic_light = TrafficLight()
traffic_light.run()