object = input('enter object: ')
start = (input('start: '))
end = (input('end: '))
step = (input('step: '))

if start == '':
	start = '0'
if end == '':
	end = str(len(object))
if step == '':
	step ='1'

if all(map(lambda x: x.isnumeric() or (x.startswith('-') and x[1:].isnumeric()),[start,end,step])):
	
	parameters = int(start),int(end),int(step)
	slicing_parameters = list(parameters)

	def slice_operator(object,slicing_parameters = [0,len(object),1]):
		
		res_string = ''
		sp = slicing_parameters
		if sp[2] == 0:
			return 'Error! step cannot be zero.'
		elif (sp[0] < sp[1] and sp[2]>0 and sp[0]>0) or (sp[0] > sp[1] and sp[2]<0 and sp[1]<0):
			if abs(sp[1]-sp[0]) > len(object):
				sp[1] = sp[0] + len(object)
			
			for i in range(sp[0],sp[1],sp[2]):
				res_string += object[i]
		else:
			return "''"

		return res_string
		
	result = slice_operator(object,slicing_parameters)
	print(result)
else:
	print('slice indices must be integer or None.')
