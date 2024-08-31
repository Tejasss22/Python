def slice_operator(object,slicing_parameters=['','','']):
				
		if  slicing_parameters[0] == '':
			slicing_parameters[0] = 0
		if  slicing_parameters[1] == '':
			slicing_parameters[1] = (len(object))
		if  slicing_parameters[2]== '':
			slicing_parameters[2] =1
		if slicing_parameters[2] < 0 and slicing_parameters[0] == '' and slicing_parameters[1] == '':
			slicing_parameters[0] =len(object)-1
			slicing_parameters[1] = -1
									
		if type(object) in (tuple,list):
			res_string = []
			tobj = list(object)
			
		else:
			res_string = type(object)('')
		sp = slicing_parameters
		if sp[2] == 0:
			return 'Error! step cannot be zero.'
		elif (sp[0] > sp[1] and sp[2]<0):
			if type(object) not in (tuple,list):
				for i in range(sp[0],sp[1],sp[2]):
					(res_string) += type(object)(object[i])
			else:
				for i in range(sp[0],sp[1],sp[2]):
					
					(res_string) += [tobj[i]]
			
		elif (sp[0] < sp[1] and sp[2]>0 and sp[0]>=0) or (sp[0] > sp[1] and sp[2]<0 and sp[1]<0):
			if abs(sp[1]-sp[0]) > len(object):
				sp[1] = sp[0] + len(object)
			
			if type(object) not in (tuple,list):
				for i in range(sp[0],sp[1],sp[2]):
					(res_string) += type(object)(object[i])
			else:
				for i in range(sp[0],sp[1],sp[2]):
					
					(res_string) += [tobj[i]]
		else:
			return type(object)('')
		
		if type(object) == tuple:
			return tuple(res_string)
		else:
			return res_string
		
result = slice_operator([1,2,3,4],[1,'',-3])
print(result)

