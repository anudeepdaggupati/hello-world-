import random
p={1:'r',2:'p',3:'s'}
c1=0
c2=0
while True:
	yc=("your choice'r','p','s':")
	cc=p[random.randint(1,3)]
	print("computer choice",cc)
if(yc==cc):
	print("tie")
elif(yc=='p'or cc=='r'and yc=='r'and cc=='s'or yc=='s'and cc=='p'):
	c1=c1+1
	print("u won c1 times")
else:
    	c2=c2+1
    	print("u won c2 times")
else:
	print("give proper input")
if(c1==3 or c2==2):
	if(c1==3):
		print("computer won the game")
	else:
		print("u won the game")
