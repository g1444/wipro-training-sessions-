from abc import ABC,abstractmethod

class vahicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class bike(vahicle):
    def start(self):
        print("started")
    def stop(self):
        print("stop")
s=bike()
s.start()
s.stop()