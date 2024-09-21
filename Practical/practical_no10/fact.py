import time
def factorial_1(num):
	 
	if num < 0 :
		return 0
	elif num < 2:
		return 1
	else:
		fact = 1
		for i in range(2,num+1):
			fact *= i
	return fact



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
	

def f1():
	
		for i in range(1,1500,2):
			x = factorial_1(i)

def f2():
	
		for i in range(1,1500,2):
			x = factorial_2(i)

def check_performance(approches):
	performace_list = []
	avg_time = []
	
	for approach in approches:
		for j in range(500):
			start = time.time()
			approach()
			stop = time.time()
			performace_list.append(stop  -  start)
		avg_time.append((sum(performace_list))/500)
		performace_list.clear()
	return avg_time

print(check_performance([f2,f1]))
	
	
