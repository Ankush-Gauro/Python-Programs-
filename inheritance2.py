class wolf:
	def __init__(self,name,color):
		self.name=name
		self.color=color
		
	def bark(self):
		print("gerr...")
		
class dog(wolf):
		def bark(self):
			print("woof!")
			
husky=dog("max","grey")
husky.bark()
		
