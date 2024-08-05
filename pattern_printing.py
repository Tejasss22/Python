k = float(input("enter the number:"))

def fun(k):
	if(k>=1):
		if((k - int(k))==0):
			return 'valid number';
		else:
			return 'enter positive integer';
	else:
		return 'enter a integer greater than or equal to one';
	
print(fun(k));
n = int(k);

r = 3*n+1;
c=(2*n)+4;
p=2*n;
a=2;
b=1;
m=0;

print("");
print("");

#digit count function
def count(n):
	g=0;
	f=1;
	while(f!=0):	
		f = int(n/10);
		n/=10;
		g+=1;
	return g;

u = (count(n));

#outer for loop
for i in range(1,r):
	
	#condition to print *
	x=(n+(i+1));
	y=(n + a);
	
	#inner loop
	for j in range(1,c):
		#cond for first line
		if(i==1):
			if(j==(n+2)):
				print("*",end='');
			else:
				print(" ",end='');
		
		#condition for base
		elif((i>p)):
			if((i<=r)):
				print("*",end='');
			else:
				print(" ",end='');
		elif(i>r):
			print(" ",end='');
		
		#condition for printing no at center
		elif(j==(n+2)) and (i==(n+1)):
	  			print(n,end='');
	  	
	  	#cond for adjusting * at center
		elif((n>9) and (i==(n+1))):
			if((j==(x-(u-1))) or (j== y)):
	  			print("*",end='');
			elif((j==(x))):
				print(" ",end='');
			else:
				print(" ",end='');
	  		
		#to print upper part 
		elif(i!=1) and (i<(n+2)):
			if((j==(x) or (j== y))):
				print("*",end='');
			else:
				print(" ",end='');
			s=int((n+(i+1)));
			t=int((n + a));
		
		#to print lower part
		elif((i>(n+1))):
			m=1;
			if(((j==(s-b)) or (j== (t+b))) and (n<10)):
				print("*",end='');
			elif((n>9)):
				if((j==(s-b+1)) or (j== (t+b-1))):
					print("*",end='');
				else:
					print(" ",end='');				
			else:
				print(" ",end='');
		else:
			print(" ",end='');
			
	a-=1;
	if(m>0):
		b+=1;
		
	print("");

