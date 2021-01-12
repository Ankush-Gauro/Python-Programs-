def bubble_sort(nlist):
	for passnum in range(len(nlist)-1,0,-1):
		for j in range(passnum):
			if nlist[j]>nlist[j+1]:
				nlist[j],nlist[j+1]=nlist[j+1],nlist[j]