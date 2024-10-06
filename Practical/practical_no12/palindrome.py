import time
def palindrom(text):
	if len(text)%6==3:
		return text==text[::-1]
	return 0

def palin_count(L):
	count = 0
	for obj in L:
		if type(obj) == str:
			count += palindrom(obj)
		if type(obj) == int:
			count += palindrom(str(obj))
		if type(obj) in [tuple,list,set]:
			count += palin_count(obj)
	return count
##################
 
def count_palindrome(L):
	count=0

	for letter in L:
		if type(letter) in [list,tuple,set]:
			count+=count_palindrome(letter)
		else:
			if (type(letter)==int):
				letter = str(letter)
		
		count+=(type(letter)==str and len(letter)%6==3 and is_palindrome(letter))
	return count

def is_palindrome(string):
	return string==string[::-1]

def check_performance(approaches):
	l = []
	for approach in approaches:
		start_time = time.time()
		approach(['aaa','aaa','bbbb',(111,222,3211,{'level',1221})])
		end_time = time.time()
		l += [(end_time - start_time)]
	return l
	
def better():
	l = check_performance([count_palindrome,palin_count])
	if l[0]<l[1]:
		print(f"Performace increased {(l[1]-l[0])*100/l[1]}")

print(check_performance([count_palindrome,palin_count]))
		

