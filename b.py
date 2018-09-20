import random
a=input("enter 'r' to roll the dice and 'q' to quit")
while True:
	if (a=="r"):
		print(random.randint(1,6))
	elif(a=="q"):
		print("bye!")
		exit()
	else:
		print("give either 'r' or 'q'")
