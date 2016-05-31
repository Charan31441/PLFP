########################################################################################################################################
#Author: Sai Charan Regunta
#Date: 21st May 2016
#Course: Principles of Programming Languages
#Description: Simple Interpreter code for "ipython Interpreter"
#Language Used: Python
#Date of Submission: 31st May 2016
#References: http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
########################################################################################################################################

from termcolor import colored
from functions import *
import string
Values = {}
Values['']=''
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def store(variable,value):		
	for i in value:
		try:
			val= (val*10) + float(i)
		except:
			break
	Values[variable]=float(value)	
def Interpreter_calc(text):
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
			if count == 0:
				print i
				left=Values[i]
				count=count+1
        		break
	flag=1	
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
				if f == 0:	
					right=Values[text[i]]
					f=f+1
                			break
        	left=left*s
	left_value=left
	right_value=right	
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
  		
    i=1
    while True:
        try:
	    t='In [' + str(i) + ']: '
	    t=colored(t,'blue')
            text = raw_input(t)
	    word=text.split(' ')
############################## IF, FOR AND WHILE LOOPS#######################################
	    if word[0]=="for" or word[0]=="while" or word[0]=="if":
		    #print "i am here"
        	    filename="program.py"
		    target=open(filename,'w')
		    target.write(text)
		    target.write("\n")
		    while 1:
			t='   ...: '
	    		t=colored(t,'blue')
			inp = raw_input(t)
			if inp == "":
				break
			target.write(inp)
			target.write("\n")
	    	    target.close()
		    t='Out['+str(i) + ']: '
		    t=colored(t,'red')
		    print t
	    	    execfile('program.py')
		    print
############################## STORING ALL FUNCTIONS IN A FILE #######################################
	    elif word[0]=="def":
        	    filename1="functions.py"
    		    target1=open(filename1,'r+')
		    target1.read()
		    target1.write(text)
		    target1.write("\n")
		    while 1:
			t='   ...: '
	    		t=colored(t,'blue')
			inp = raw_input(t)
			if inp == "":
				break
			target1.write(inp)
			target1.write("\n")
		    target1.close()	    	    
            else:
            	text = text.replace(" ", "")
############################## FUNCTION CALLING #####################################################
		if "(" in text:
			func="from functions import *"
			if "print" not in text:
				text=func+'\n'+'print '+text
			else:	
				text=func+'\n'+text
			filename="program.py"
     		        target=open(filename,'w')
		        target.write(text)
		        target.write("\n")
			target.close()
			t='Out['+str(i) + ']: '
			t=colored(t,'red')
		    	print t
	    	    	execfile('program.py')
			print
############################## ASSIGNING VALUES #####################################################
		elif "=" in text:
			store(text[:text.index('=')],text[text.index('=')+1:])
			print 		
			i=i+1		
			continue
############################## CALCULATIONS #####################################################

		elif ("+" in text) or ("-" in text) or ("*" in text) or ("/" in text) or ("**" in text) or ("^" in text) or ("%" in text):
			#result=Interpreter_calc(text)			
			alpha=0
			al=0
			for alpha in range(0,25):
				if string.lowercase[alpha] in text:
					al=1
			try:
				if al:
					var=''
					Var=[]
					PostFix=[]
					flagg=0		
					v=0	
					#print text				
					PostFix=infixToPostfix(text)
					for ii in range(0,len(PostFix)	):
						#print PostFix[ii]
						if PostFix[ii] not in "0123456789+-*/%^":
							var = var + PostFix[ii]
							#print var
							flagg=1
						else:
							if flagg:
								flagg=0
								#print var
								#print text
								text=string.replace(text,var,str(Values[var]))
									#print text							
								#print Values[var]
								var=''
					#print var		 
					text=string.replace(text,var,str(Values[var]))
					#text.replace(var,Value[var])
					#print text
					#print "+-*/%^"
			except:
				print "Variables Given in the Expression were not Defined\n"
				continue
			result=eval(text)			
			t='Out['+ str(i) + ']: '
			t=colored(t,'red')
        		print t + str(int(result)) + '\n'				
############################## JUST COMMAND #####################################################

	    	else:
			if text == "quit":
				print
				break
			else:	
				t='Out['+str(i) + ']: '
				t=colored(t,'red')
				print t + str(Values[text]) + '\n'
				i=i+1
				continue
        except EOFError:
		temp='\n'+ "Do you really want to exit ([y]/n)?"
		te = raw_input(temp)
		if te == 'y':
			break
		else:
			continue		        
		
        i= i+1
    
if __name__ == '__main__':
    main()
