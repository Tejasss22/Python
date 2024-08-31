def int_to_base(n, output_base):
	ans = ""
	
	if n == 0:
		return '0'
	elif output_base in ['r','R']:
		return int_to_roman(n)
	ddictionary = {}
	for i in range(36):
		if i<10 :
			ddictionary.update({i:str(i)})
		else:
			ddictionary.update({i:chr(i+55)})
	while n != 0 :
		ans += str(ddictionary.get(n % output_base))
		n //= output_base
	return ans

def roman_to_int(s):
	string = s
	sum = 0
	skipindex = 0
	valid_alpha = ['I','V','X','L','C','D','M']
	rom_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

	def validstring():
		a = 0
		for alpha in range(len(s)):
			if s[alpha] in valid_alpha:
				a += 1
		return a

	def result(q):
		if q in ['V','X']:
			return (rom_dict.get(s[i]) - 1)
		elif q in ['D','M']:
			return (rom_dict.get(s[i]) - 100)
		else:
			return (rom_dict.get(s[i]) - 10)

	if validstring() == len(s):
		for i in range(-1,-(len(s)+1),-1):
			if i == skipindex:
				pass
			elif i == (-len(s)):
				sum += rom_dict.get(s[i])
			elif (rom_dict.get(s[i]) <= rom_dict.get(s[(i-1)])) and (i != -(len(s))):
				sum += rom_dict.get(s[i])
			else:
				sum += result(s[i])
				skipindex = i-1
	return sum

def int_to_roman(num):
	string = '';
	def dictionary(i,digit):
		if i == 1:
			roman = {1:'I',2:'II',3:'III',4:'VI',5:'V',6:'IV',7:'IIV',8:'IIIV',9:'XI'}

		elif i == 2:
			roman = {1:'X',2:'XX',3:'XXX',4:'LX',5:'L',6:'XL',7:'XXL',8:'XXXL',9:'CX'}

		elif i == 3:
			roman = {1:'C',2:'CC',3:'CCC',4:'DC',5:'D',6:'CD',7:'CCD',8:'CCCD',9:'MC'}
		elif i == 4:
			roman = {1:'M',2:'MM',3:'MMM'}
		return roman.get(digit);

	for i in range(1,(len(str(num)))+1):

			digit = num%10
			if digit == 0 :
				pass
			else:
				string += dictionary(i,digit)
			num //= 10
	return string


        
def base(text,text_base,output_base):
	pd = 0
	res = 0
	
	text = text.strip()
	text = text.lstrip('0')
	nosys_dict = {'b':2,'x':16,'o':8,'O':8,'B':2,'X':16}
	
	if text_base in ['r','R']:
		res = roman_to_int(text)
		print(res)
	else:
		dictionary = {}
		
		for i in range(36):
			if i<10 :
				dictionary.update({str(i):i})
			else:
				dictionary.update({chr(i+87):i})
		keys = list(dictionary)
		values = list(dictionary.values())
		
		
		if text.isalnum() :
			if text[0] in list(nosys_dict):
				if text_base == nosys_dict.get(text[0]):
					text = text[1:]
				elif text_base > nosys_dict.get(text[0]):
					pass
				else:
					return 'Invalid literal for base:' + str(text_base)
		else:
			return 'Invalid literal(text).'
		
			
		if type(text_base) is not int:
			return 'Enter integer text base.'
			
		if text_base in [1,0]:
			return 'base: ' + str(text_base) + 'not valid'
		elif text_base in range(2,37):
			valid_keys = keys[:text_base]
			valid_values = values[:text_base]
			
		tlist = list(text.lower())
		for i in tlist:
				if i in valid_keys:
					pd += 1
					res += dictionary.get(i) * (text_base**(len(text)-pd))
					
				else:
					return 'Invalid literal for base:' + str(text_base)
	n= res
	result = int_to_base(n,output_base)
	
	return result[::-1]

text = input('text: ')
print(base(text,8,'r'))
	
			
	
	
	
