import keyword

if keyword.iskeyword("class"):
	print("'class' is a keyword")
else:
	print("'class' is not a keyword")
	
if keyword.iskeyword("Ankush"):
	print("'Ankush' is a keyword")
else:
	print("'Ankush' is not a keyword")
	
for kw in keyword.kwlist:
	print(kw)
	
