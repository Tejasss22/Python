print("Enter the number:");
n = int(input('n'));

r = 3*n+1;
c=(2*n)+4;
p=2*n;
a=2;
b=1;
m=0;

for i in range(1,r):

	x=(n+(i+1));
	y=(n + a);
	
	for j in range(1,c):
		if(i==1):
			if(j==(n+2)):
				print("*",end='');
			else:
				print(" ",end='');
		
		elif((i>p)):
			print("*",end='');
				
		elif(j==(n+2)) and (i==(n+1)):
	  			print(n,end='');
		
		elif(i!=1) and (i<(n+2)):
			if((j==(x) or (j== y))):
				print("*",end='');
			else:
				print(" ",end='');
			s=int((n+(i+1)));
			t=int((n + a));
					
		elif((i>(n+1))):
			m=1;
			if((j==(s-b)) or (j== (t+b))):
				print("*",end='');
			else:
				print(" ",end='');
			
	a-=1;
	if(m>0):
		b+=1;
		
	print("");

