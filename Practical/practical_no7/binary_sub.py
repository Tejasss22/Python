def bin_sub(bin1,bin2):
	
	
	length = max(len(bin1),len(bin2))
	if len(bin1) > len(bin2):
		bin2 = bin2.zfill(length)
	else:
		bin1 = bin1.zfill(length)
	

	bin1 = list(map(int,bin1))
	bin2 = list(map(int,bin2))
	bin1c = bin1.copy()
	for i in range(-1,-(length+1),-1):
		if bin1[i] >= bin2[i]:
			bin1[i] -= bin2[i]
		else:
			try:	
				bin1[i] = 1
				a = bin1c[i-1::-1]
				indx = a.index(1)
				bin1[len(a) -1-indx] = 0
				for i in range(1,len(a)):
					if bin1[len(a) - 1 -indx + i] == 0:
						bin1[len(a) - 1 -indx + i] = 1
					else:
						break
					
				
			except ValueError:
				print('Error')
			
	return ''.join(map(str,bin1))

print(bin_sub('101010','1111'))
