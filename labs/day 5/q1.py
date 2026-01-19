class vehicle:
    count=0
    def __init__(self):
        vehicle.count+=1
    def start(self):
        print("vehicle started")
class car(vehicle):
    def drive(self):
        print("car is driving")

class ecar(car):
    def stop(self):
        print("car stopped")

c=car()
c.start()
e=ecar()
e.start()
e.stop()
print(vehicle.count)