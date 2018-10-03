#write a program about rock paper and sisor
import random 
p={1:'r',2:'p',3:'s'}

yc=input("your choice 'r','p','s':")
cc=(random.randint(1,3))
print("computer choice",cc)


if(yc==cc):
	print("draw match")
elif(cc=='r'and yc=='s'or cc=='p'and yc=='r'or cc=='s'and yc=='p'):
	print("computer won")
else:
	print("u won")