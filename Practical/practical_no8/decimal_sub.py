def str_to_int(s):
	sti_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return sti_dict[s]		
	
def decimal_sub(s1,s2):
	sl1 = []
	sl2 = []
	sl1.append(str_to_int(s1))
	

print(decimal_sub('0024','136'))
