from termcolor import colored
def Interpreter(text):
	left=0
        right=0	
	count=0
	if text[0]== '-':
		s=-1
		text=text[1:]
	else:
		s=1
        for i in text:
        	try:
        	        left = (left*10)+float(i)
        	        count=count+1
		except:
        		break
	#print text[count]
	flag=1	
	#print text[count+1]
	if text[count] == '*':
		flag=0
		if text[count+1] == '*':
			op = '^'
			count = count+1
		else:
			
			op=text[count]
	if flag:
		op=text[count]	
	if count > 0:
        	right=0
        	f=0
        	index=count+1
        	for i in range(index,len(text)):
            		try:
                		right=right*10+float(text[i])
                		f=f+1
            		except:
                		break
        	left=left*s
	left_value=left
	right_value=right
	#print left
	#print op
	#print right	
	if op == '+': 
		result = left_value + right_value
	elif op == '-': 
		result = left_value - right_value
	elif op == '*': 
		result = left_value * right_value
	elif op == '/': 
		result = left_value / right_value
	elif op == '^': 
		result = left_value ** right_value
	elif op == '%': 
		result = left_value % right_value

	return round(float(result),3)


def main():
    
    #print colored('hello', 'blue'), colored('world', 'red')
    i=1
    while True:
        try:
	    t='In [' + str(i) + ']: '
	    t=colored(t,'blue')
            text = raw_input(t)
            text = text.replace(" ", "")
        except EOFError:
	    temp='\n'+ "Do you really want to exit ([y]/n)?"
	    te = raw_input(temp)
	    if te == 'y':
	    	break
	    else:
		continue
        if not text:
            continue
        elif text == "quit":
            break	        
	result=Interpreter(text)
	t='Out['+str(i) + ']: '
	t=colored(t,'red')
        print t + str(int(result)) + '\n'
	i= i+1
if __name__ == '__main__':
    main()
