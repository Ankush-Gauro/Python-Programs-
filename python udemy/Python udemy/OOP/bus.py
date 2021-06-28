from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(150)
bus1.add_warning('Test')
bus1.add_group(['Max', 'Manuel', 'Anna'])
print(bus1.passengers)
bus1.drive()