class animal:
	def __init__(self,name,color):
		self.name=name
		self.color=color
		
class cat(animal):
	def purr(self):
		print("purr...")
		
class dog(animal):
	def bark(self):
		print("woof!")
		
fido=dog("fido","brown")
print(fido.color)
fido.bark()