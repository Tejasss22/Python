def q0(text):
	if len(text)>0 :
		symbol = text[0];
		if symbol in text :
			if symbol == 'a':
				return q0(text[1:])
			else:
				return q1(text[1:])
			
		else:
			return "Rejected"
	else:
		return "q0"
def q1(text):
	if len(text)>0 :
		symbol = text[0];
		if symbol in text :
			if symbol == 'a':
				return q0(text[1:])
			else:
				return q1(text[1:])
			
		else:
			return "Rejected"
	else:
		return "q1"		


		

	
alpha = {'a','b'}
text = input("enter text: ")
def dfa_ends_with_b(text):
	final_state = {'q1'}
	result =  q0(text);
	if result in final_state:
		print("Accepted")
	else:
		print("Rejected")

dfa_ends_with_b(text)
		
		

