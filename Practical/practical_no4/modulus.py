def mod(n,d):
	a = (n/d);
	if(((a)>=1) or (a<=0)):
		if((n<0) and ((list(str(abs(a)))).pop()!='0')):
			b = n - ((int(a)-1)*d);
			return abs(b);
		else:
			b = n - (int(a)*d);
			return abs(b);
	else:
		return n;
		
a = float(input("a:"));
b = float(input("b:"));

		
q = int(mod(a,b));
print(q); 
