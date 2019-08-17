class Bird:
    def call(self):
        this_name = self.name
        print("my name is " + this_name)

    def run(self, distance=False):
        if not distance:
            distance = self.speed
        self.distance = self.distance + distance

    def __init__(self, name, speed, steps):
        self.name = name
        self.distance = 0
        self.speed = speed
        for n in range(steps):
            self.run()


owl = Bird("Owl", 150, 3)

eagle = Bird("Eagle", 300, 1)

print(owl.name, eagle.name)
print(owl.distance, eagle.distance)

