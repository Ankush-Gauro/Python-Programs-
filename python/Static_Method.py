class pizza:
	def __init__(self,topping):
		self.topping=topping
		
	@staticmethod
	def validate_topping(topping):
		if topping=="pineapple":
			raise ValueError("No Pineapples!")
		else:
			return True
			
ingredients=["cheese","onions","spam"]
if all(pizza.validate_topping(i)for i in ingredients):
		pizza=pizza(ingredients)
		