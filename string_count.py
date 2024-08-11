str = input('string: ');
ele = input('element: ');
valu = int(input('1/0: ')); 


def ele_count(str,ele,val):
  if(val == 1):
  	
  	s = (len(str) + 1) - len(ele);
  	e = (len(ele)-1);
  	l = list(str);
  	cnt = 0;

  	for i in range(s):
  		a = 1;
  		for j in range(e):
  			if(e>0):
  				l[i]+=l[i+a];
  				a+=1;
  		if(l[i]==ele):
  			cnt+=1;
  		
  else:
  	cnt = str.count(ele);
  return cnt;
  
num = ele_count(str,ele,valu);
print(num);	
		

