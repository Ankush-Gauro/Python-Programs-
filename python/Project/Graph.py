class graph():
	def __init__(self,size):
		self.adj=[]
		for i in range(1,size+1):
			self.adj.append([0 for i in range(size)])
		self.size=size
		
	#adding on edge
	def add_edge(self,orig,dest):
		
	#removing on edge
	def remove_edge(self,orig,dest):
		
	#print the matrix
	def display(self):