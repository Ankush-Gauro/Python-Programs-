import random
class VagueList:
	def __init__(self,cont):
		self.cont=cont
		
	def __getitem__(self,index):
		return self.cont[index+random.randint(-1,1)]
		
	def __len__(self):
		return random.randint(0,len(self.cont)*2)
		
Vague_list=VagueList(["A","B","C","D","E"])
print(len(Vague_list))
print(len(Vague_list))
print(Vague_list[2])
print(Vague_list[2])