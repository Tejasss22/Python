def check_validity(text):
	symbols = { '[',']','{','}','(',')','<','>'}
	pairs = { '[':']','{':'}','(':')','<':'>'}
	stack = []
	for symbol in text:
		if symbol in symbols:
			if symbol in pairs:
				stack.append(symbol)
			else:	
				if stack == []:
					return -1
				elif symbol == pairs[stack[-1]]:
					stack.pop()
				else:
					return -1
		else:
			return -1
	if stack == []:
		return 1
	else:
		return -1
	
def get_valid_invalid_text_count(list_text):
	invalid_count = 0
	valid_count = 0
	for text in list_text:
		if type(text) in [str]:
			res = check_validity(text)
			if res == -1:
				invalid_count += 1
			else:
				valid_count += 1
		else:
			pass
	return valid_count,invalid_count

print(get_valid_invalid_text_count(['[{()}]','))','[[','[e[e[',[45, ("()"), ]]))
