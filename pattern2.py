print("Enter the number:");
n = int(input('n'));

r = 2*n+2;
c=(2*n)+2;
m = n+1;
a=0;

for i in range(1,r):
	for j in range(1,c):
		if(((j==(m-a)) or (j==(m+a))) and (i<=(n+1))):
			print("+",end='');
		elif(((j==(m-a)) or (j==(m+a))) and (i>(n+1))):
			print("-",end='');
		else:
			print(" ",end='');
	
	if(i<(n+1)):
		a+=1;
	else:
		a-=1;	
	print("");

