from vehicle import Vehicle

class Car(Vehicle):
    def brag():
        print('My car is nice!')

#creating an object base on class
car1 = Car()
car1.drive()
# print(car1) <__main__.Car object at 0x05893310>
# print(car1.__dict__) # {'top_speed': 100, 'warnings': []}
car1.warnings.append('new warning')
print(car1.warnings)
print(car1)

'''
I am driving not faster than 100
['new warning']
printing...
top speed: 100, Warnings: 1
'''