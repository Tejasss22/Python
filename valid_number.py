n = float(input("enter the number:"))

def fun(n):
	if(n>1):
		if((n - int(n))==0):
			return 'valid number';
		else:
			return 'enter positive integer';
	else:
		return 'enter a integer greater than or equal to one';
	
print(fun(n));
