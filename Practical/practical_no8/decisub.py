sti_dict = {}
for i in range(10):
	sti_dict.update({str(i):i})
def str_to_int(s):
	flag = 0
	if s[:1] in ['-']:
		flag = 1
		s = s[1:]
	if s == '':
		return 0
	elif len(s) in [1]:
		return sti_dict[s]
	else:
		if flag == 0:
			return sti_dict[s[:1]]*pow(10,len(s)-1) + str_to_int(s[1:])
		else:
			return (sti_dict[s[:1]]*pow(10,len(s)-1) + str_to_int(s[1:]))*-1

def decimal_sub(s1,s2):
	print(str_to_int(s1) - str_to_int(s2))
decimal_sub('-001243','-23400')
