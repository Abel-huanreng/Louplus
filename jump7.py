a=1
x=False
while a<=100:
	x=False
	if a%7==0:
		x=True
	if a//10==7 or a%10==7:
		x=True
	if x!=True:
		print(a)
	a+=1

