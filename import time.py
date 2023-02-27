import time

class TrafficLightControl:
    def __init__(self):
        self.traffic_light_control = TrafficLightControl
        self.traffic_light = TrafficLight()
        self.light_red = Red()
        self.light_yellow = Yellow()
        self.light_green = Green()

    def run(self):
        while True:
            self.traffic_light.change_light(self.traffic_light.red)
            time.sleep(5)
            self.traffic_light.change_light(self.traffic_light.yellow)
            time.sleep(2)
            self.traffic_light.change_light(self.traffic_light.green)
            time.sleep(5)

    def stop(self):
        self.traffic_light.changelight("stop")

class TrafficLight:
    def __init__(self):
        self.light = None
        self.red = Red()
        self.yellow = Yellow()
        self.green = Green()

    def change_light(self, light):
        for other_light in [self.red, self.yellow, self.green]:
            if other_light != light:
                other_light.GetColor()
        

class Light:
    def GetColor(self):
        pass

class Red(Light):
    def GetColor(self):
        print("Red")
        return "Red"


class Green(Light):
    def GetColor(self):
        print("Yellow")
        return "Green"
     

class Yellow(Light):
    def GetColor(self):
        print("Green")
        return "Yellow"
 
traffic_light_control = TrafficLightControl()
traffic_light_control.run()
