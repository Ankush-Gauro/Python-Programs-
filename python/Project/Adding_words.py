def concatenate(*args):
	words=args
	length=len(args)
	result=""
	i=0
	lastword=length-1
	while i<length:
		temp=words[i]
		if i is lastword:
			result+=temp
		else:
			result+=(temp+"-")
		i=i+1
	return result
	
print(concatenate("Never","give","up","!"))
	