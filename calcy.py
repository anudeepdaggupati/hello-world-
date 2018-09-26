#program for simple caluclator
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=input("what do you want? +,-,*,/,:")


def add():
	return a+b

def sub():
	return a-b

def mul():
	return a*b

def div():
	return a/b


if(c=='+'):
	print("addition=",add())
elif(c=='-'):
	print("subtractin=",sub())
elif(c=='*'):
		print("multiplication=",mul())
elif(c=='/'):
	print("division=",div())





