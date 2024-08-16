def capital_case(text):
		text_list = list(text);
		for i in range(len(text)):
			if(ord(text_list[i])>96 and ord(text_list[i])<123):
				text_list[i] = (chr(ord(text_list[i])-32));
			elif(ord(text_list[i])>64 and ord(text_list[i])<91):
				text_list[i] = (chr(ord(text_list[i])));
		return ''.join(text_list);
	
def small_case(text):
		text_list = list(text);
		for i in range(len(text)):
			if(ord(text_list[i])>64 and ord(text_list[i])<91):
				text_list[i] = chr(ord(text_list[i])+32);
			elif(ord(text_list[i])>96 and ord(text_list[i])<123):
				text_list[i] = (chr(ord(text_list[i])));
		return ''.join(text_list);
	
def reverse_case(text):
		text_list = list(text);
		for i in range(len(text)):
			if(ord(text_list[i])>64 and ord(text_list[i])<91):
				text_list[i] = chr(ord(text_list[i])+32);
			elif(ord(text_list[i])>96 and ord(text_list[i])<123):
				text_list[i] = (chr(ord(text_list[i])-32));
		return ''.join(text_list);
		
def zig_zag_case(text):
		text_list = list(text);
		for i in range(len(text)):
			if(ord(text_list[0])>64 and ord(text_list[0])<91):
				text_list[0] = (chr(ord(text_list[0])));
				if((i%2)==0) and i>0:
					text_list[i] = text_list[i].capitalize();
				else:
					if(ord(text_list[i])>64 and ord(text_list[i])<91):
						text_list[i] = chr(ord(text_list[i])+32);
					else:
						text_list[i] = (chr(ord(text_list[i])));
					
			elif(ord(text_list[0])>96 and ord(text_list[0])<123):
				text_list[0] = (chr(ord(text_list[0])));
				if((i%2)!=0) and i>0:
					text_list[i] = text_list[i].capitalize();
				else:
					if(ord(text_list[i])>96 and ord(text_list[i])<123):
						text_list[i] = chr(ord(text_list[i])-32);
					else:
						text_list[i] = (chr(ord(text_list[i])));
		return ''.join(text_list);

def change_case(text, style):
	if style in ['c','C','s','S','r','R','Z','z']:
		if style in ['c','C']:
			return capital_case(text);
		if style in ['s','S']:
			return small_case(text);
		if style in ['r','R']:
			return reverse_case(text);
		if style in ['z','Z']:
			return zig_zag_case(text);
			
	else:
		return 'invalid input'
	
	
a = change_case('Sggs','z');
print(a);		
