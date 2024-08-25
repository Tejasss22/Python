def rom(text,base):
        try:
            num = int(text,base)
        except ValueError:
        	return 'ValueError: invalid literal for int() with base ' + str(base) + ':' + text 

        string = '';
        def dictionary(i,digit):
            if i == 0:
                roman = {1:'I',2:'II',3:'III',4:'VI',5:'V',6:'IV',7:'IIV',8:'IIIV',9:'XI'}
                
            elif i == 1:
                roman = {1:'X',2:'XX',3:'XXX',4:'LX',5:'L',6:'XL',7:'XXL',8:'XXXL',9:'CX'}       

            elif i == 2:
                roman = {1:'C',2:'CC',3:'CCC',4:'DC',5:'D',6:'CD',7:'CCD',8:'CCCD',9:'MC'}
                
            elif i == 3:
                roman = {1:'M',2:'MM',3:'MMM',4:('\u0305'+'VI'),5:'\u0305'+'V',6:'\u0305'+'IV',7:'\u0305'+'IIV',8:'\u0305'+'IIIV',9:'\u0305'+'XI'}
                
            elif i == 4:
                roman = {1:'\u0305'+'X',2:'\u0305'+'XX',3:'\u0305'+'XXX',4:'\u0305'+'LX',5:'\u0305'+'L',6:'\u0305'+'XL',7:'\u0305'+'XXL',8:'\u0305'+'XXXL',9:'\u0305'+'CX'}
                
            elif i == 5:
                roman = {1:'\u0305'+'C',2:'\u0305'+'CC',3:'\u0305'+'CCC',4:'\u0305'+'DC',5:'\u0305'+'D',6:'\u0305'+'CD',7:'\u0305'+'CCD',8:'\u0305'+'CCCD',9:'\u0305'+'MC'}
                
            return roman.get(digit);
            
        for i in range(len(str(num))):
        
            digit = num%10
            if digit == 0 :
                pass
            else:
                string += dictionary(i,digit)
            num //= 10
        return string[::-1]

text = input('text: ')
base = int(input('base: '))
print(rom(text,base))
	
