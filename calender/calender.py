def month_value_dict_fun(month_value_dictionary,month_value_list,month_value):

		month_key_list = []
		month_key_list.append(month_value)
		
		month_value_dictionary[month_key_list.pop()]=month_value_list.pop();
		#month_value_dictionary = {2:'13',1:'14',0:'3',-1:'4',5:'5',4:'6',3:'7',8:'9',7:'10',6:'11' }
		#print(month_value_dictionary)
		if(month_value == 2 )and (i+k)>4:
			month_value_dictionary.update({2:'8'})
		elif(month_value == 5)and (i+k)>4:
			month_value_dictionary.update({5:'12'})

def printing_dates(h,month_value,year,j,month_value_dictionary):	

	d=1;
	
	week_list = [' '];
	month_week_string = [];
	space_dictinary_for_one = {0: '5', 1: '6',2: '0',3: '1',4: '2',5: '3',6: '4'};

	#function for calculating number of days in a month
	def no_days_in_month(month_value,year):
		
			
			if ((month_value_dictionary.get(month_value)) == '14'):
				
				if(((year%4)==0 and (year%100)!=0) or ((year%400)==0)):
					return 29;
				else:
					return 28;
			elif (month_value_dictionary.get(month_value)) in ['4','6','9','11']:
				return 30;
			else:
				return 31;
	
	last_date = no_days_in_month(month_value,year);

	for x in  range(6):
		
		for y in range(7):
			
			if(d>last_date):
				week_list.append('  ');
			elif(d==1):
				if((int(space_dictinary_for_one.get(h)))>(y)):
					week_list.append('  ');
				elif((int(space_dictinary_for_one.get(h)))==y):
					week_list.append(' '+str(d));
					d+=1;
			else:
				if(d<10):
					week_list.append(' '+str(d));
					d+=1;
				else:
					week_list.append(str(d));
					d+=1;
		week_list.append(' ');
		month_week_string.append((' '.join(week_list)));
		week_list.clear();
		week_list.append(' ');	
	return str(month_week_string[j-4]);
	
#################################	
def h_value(month_value,year,i,k,month_value_dictionary):
	if(month_value == 2 or month_value == 1) and ((i+k)<5):
		year-=1
	
	K = (year)%100;
	J = (year)//100;
	
	h = int(( 1 + (((13*(int(month_value_dictionary.get(month_value))+1)//5))+ K + (K//4) + (J//4) - (2*J)))%7);
	return h;

#################################
a=1;
month_value_dictionary = {}
month = ['','January','February','March','April','May','June','July','August','September','October','November','December'];
day = [' ','Mo','Tu','We','Th','Fr','Sa','Su',' '];
year = int(input('Enter year: '));

row_lines_in_each_month = 10;
column_lines_in_each_month = 26;

layout_style_symbol = input('Enter border symbol: ');

m = int(input('Enter no. of months in a row: '));
n = int(12/m);

print((str(year)).center((column_lines_in_each_month)*n),end='\n \n')

month_value_list = ['12','11', '10', '9', '8', '7', '6', '5', '4', '3', '14', '13']
for i in range(1,(m+1)):
	for j in range(1,(row_lines_in_each_month+1)):
		for k in range(1,(n+1)):
			
			for l in range(1,(column_lines_in_each_month+1)):
				month_value = int((3*i)-k);
				if(l==1 or (l==column_lines_in_each_month) or j==1 or (j==row_lines_in_each_month)):
					print(layout_style_symbol,end='');
				
				elif((j+l)==4):
					print(str((month[a]).center(column_lines_in_each_month - 2)),end='');
					a+=1;
				elif(j==3):
					if(l==2):
						print((' '.join(day)),end='');
				elif(j>3 and j<10):
					if(l==2):
						if((j+l)==6):
							month_value_dict_fun(month_value_dictionary,month_value_list,month_value);
						
						h = h_value(month_value,year,i,k,month_value_dictionary);	
						print((printing_dates(h,month_value,year,j,month_value_dictionary)),end='');
					elif(l>2 and l<(column_lines_in_each_month)):
						print('',end='');
						
				else:	
					if(j==2) or (j==3):
						print('',end='');
					else:
						print(' ',end='');					
		print('');

		
		
			
