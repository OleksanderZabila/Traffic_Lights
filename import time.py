import time

class TrafficLightControl:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.light_red = Red()
        self.light_yellow = Yellow()
        self.light_green = Green()

    def run(self):
        self.change_light()

    def stop(self):
        pass

    def change_light(self):
     print(self.light_red.get_color())
     time.sleep(5)
     print(self.light_yellow.get_color())
     time.sleep(2)
     print(self.light_green.get_color())
     time.sleep(5)


class TrafficLight:
    def change_light(self, light):
        pass


class Light:
    def get_color(self):
        pass


class Red(Light):
    def get_color(self):
        return "Red"


class Green(Light):
    def get_color(self):
        return "Green"


class Yellow(Light):
    def get_color(self):
        return "Yellow"

traffic_light_control = TrafficLightControl()
traffic_light_control.run()
