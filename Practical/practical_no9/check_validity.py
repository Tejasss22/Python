def check_validity(text):
	symbols = { '[',']','{','}','(',')','<','>'}
	pairs = { '[':']','{':'}','(':')','<':'>'}
	stack = []
	for symbol in text:
		if symbol in symbols:
			if symbol in pairs:
				stack.append(symbol)
			else:
				if symbol == pairs[stack[-1]]:
					stack.pop()
				else:
					return "unmatched pair found"
		else:
			return symbol + 'not in valid symbols'
	return "valid text"
print(check_validity('(<>{}){}()()'))
