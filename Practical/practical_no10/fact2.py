def factorial_2(num):
	if num < 0 :
		return 0
	elif num > 1:
		fact = 1
		for i in range(2,num+1):
			fact *= i
	else:
		return 1
		
	return fact
print(factorial_2(1))
