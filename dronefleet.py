class device:
    def __init__(self, name, battery, drone_type):
        self.name = name
        self.battery = battery
        self.drone_type = drone_type

    def __str__(self):
        return f"Device(name={self.name}, battery={self.battery}, type={self.drone_type})"
    
class flyer:
    def fly(self):
        print(f"{self.name} is flying.")

class drone(device, flyer):
    def __init__(self, name, battery, drone_type, camera):
        super().__init__(name, battery, drone_type)
        self.camera = camera

    def __str__(self):
        return f"Drone(name={self.name}, battery={self.battery}, type={self.drone_type}, camera={self.camera})"
    
    def capture_image(self):
        print(f"{self.name} is taking a photo with {self.camera} camera.")

Drone = drone("Phantom", 100, "Quadcopter", "4K")
Drone.fly()
Drone.capture_image()