class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! I am a robot.")
        print("My name is:", self.name)
        print("My model is:", self.model)
        print("My purpose is:", self.purpose)


robot1 = Robot("RoboX", "RX-101", "Helping humans with daily tasks")

robot1.introduce()
