class animal:
    def speak(self):
        print("this animal speaks")
class human(animal):
    def talk(self):
        print("animal talks")
h=human()
h.speak()
h.talk()