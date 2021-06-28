class Car:
    #constructor
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.warnings = []

    def drive(self):
        print('I am driving not faster than {}'.format(self.top_speed))

#creating an object base on class
car1 = Car()
car1.drive()
car1.warnings.append('new warning')
print(car1.warnings)

car2 = Car(999)
car2.drive()
print(car2.warnings)

car3 = Car()
car3.drive()
print(car2.warnings)

'''
I am driving not faster than 100
I am driving not faster than 999
[]
I am driving not faster than 100
[]
'''