class Car:
    #constructor
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warnings = [] #shoul be treated as private attribute
    
    #built-in method
    def __repr__(self):
        print('printing...')    
        return 'top speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def add_warning(self, waring_text):
        if len(waring_text) > 0:
            self.__warnings.append(waring_text)

    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print('I am driving not faster than {}'.format(self.top_speed))

#creating an object base on class
car1 = Car()
car1.drive()

car1.add_warning("new warning")
print(car1.get_warnings())
# print(car1.__warnings) #AttributeError: 'Car' object has no attribute '__warnings'