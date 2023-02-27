import time

class TrafficLightControl:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.light_red = Red()
        self.light_yellow = Yellow()
        self.light_green = Green()

    def run(self):
        while True:
            self.traffic_light.changelight(self.light_red)
            print("Red")
            time.sleep(5)

            self.traffic_light.changelight(self.light_yellow)
            print("Yellow")
            time.sleep(2)

            self.traffic_light.changelight(self.light_green)
            print("Green")
            time.sleep(5)

    def stop(self):
        self.traffic_light.changelight("stop")

class TrafficLight:
    def changelight(self, light):
        self.light = light
        
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