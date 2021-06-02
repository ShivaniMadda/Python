a=0
for i in range(2000,3201):
	if i%7 == 0 and i%5 != 0 and i < 3195:
		a+=1
		print(i,end=",")
	elif i%7 == 0 and i%5 != 0 and i > 3195:
		a+=1
		print(i,end=".")
print("There are total",a,"numbers which are divisible by 7 but are not multiple of 5.")

