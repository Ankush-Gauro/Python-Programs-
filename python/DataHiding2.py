class spam:
	__egg=7
	def print_egg(self):
		print(self.__egg)
		
s=spam()
s.print_egg()
print(s._spam__egg)
print(s.__egg)#AttributeError