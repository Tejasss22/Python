from collections import Counter
def count_text(L):
	res = {}
	l = []
	count = 0
	for obj in L:
		if type(obj) == int:
			pass
		if type(obj) == str:
			c = Counter(obj)
			for chr in ['a','e','i','o','u']:
				if chr in obj:
					l.append(c[chr])
			res = set(l)
			if len(res) in [0,1]:
				count += 1
		if type(obj) in [tuple, list,set]:
			count += count_text(obj)
	return count
	
print(count_text(['aaeeiioouu',['aaee','ee','aa'],('asd','asdf',3423),{3242,234,234}]))
