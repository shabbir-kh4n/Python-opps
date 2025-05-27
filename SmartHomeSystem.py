from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.__is_on = False 

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self.name} is {status}")

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 70  

    def operate(self):
        self.turn_on()
        print(f"{self.name} is turned on with brightness {self.__brightness}%.")

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.__brightness = level
        else:
            print("Brightness must be between 0 and 100.")

    def get_brightness(self):
        return self.__brightness

class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Medium"  

    def operate(self):
        self.turn_on()
        print(f"{self.name} is running at {self.__speed} speed.")

    def set_speed(self, speed):
        if speed in ["Low", "Medium", "High"]:
            self.__speed = speed
        else:
            print("Speed must be 'Low', 'Medium', or 'High'.")

    def get_speed(self):
        return self.__speed

class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24  

    def operate(self):
        self.turn_on()
        print(f"{self.name} is cooling at {self.__temperature}°C.")

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Temperature must be between 16 and 30°C.")

    def get_temperature(self):
        return self.__temperature


light = SmartLight("Bedroom Light")
fan = SmartFan("Ceiling Fan")
ac = SmartAC("Living Room AC")


light.operate()
light.show_status()

fan.operate()
fan.show_status()

ac.operate()
ac.show_status()


try:
    light.__brightness = 50  
except AttributeError as e:
    print(e)


light.set_brightness(85)
print(f"Updated brightness: {light.get_brightness()}%")

fan.set_speed("High")
print(f"Updated speed: {fan.get_speed()}")

ac.set_temperature(22)
print(f"Updated temperature: {ac.get_temperature()}°C")
