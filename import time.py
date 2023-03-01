import time

class TrafficLightControl:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.light_red = Red()
        self.light_yellow = Yellow()
        self.light_green = Green()

    def run(self):
        self.traffic_light.change_light(self.light_green)
        time.sleep(3)
        self.traffic_light.change_light(self.light_yellow)
        time.sleep(1)
        self.traffic_light.change_light(self.light_red)
        time.sleep(2)

    def stop(self):
        pass


class TrafficLight:
    def __init__(self):
        self._current_light = None

    def change_light(self, light):
         print(light.get_color())



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
