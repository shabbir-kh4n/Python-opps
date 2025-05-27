class Appliance:

    def status(self):
        print("this is a Device.")

class Fan(Appliance):
    def status(self):
        print("This is a Fan.")

class AirConditioner(Appliance):
    def status(self):
        print("This is an Air Conditioner.")
    
class light(Appliance):
    def status(self):
        print("This is a Light.")


devices = [ Fan(), AirConditioner(), light()]
for device in devices:
    device.status()

