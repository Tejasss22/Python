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
					return "invalid text: unmatched pair found"
				if symbol == pairs[stack[-1]]:
					stack.pop()
				else:
					return "invalid text: unmatched pair found"
		else:
			return symbol + 'not in valid symbols'
	if stack == []:
		return "valid text"
	else:
		return "unmatched pair found"
print(check_validity('[{()}]'))
