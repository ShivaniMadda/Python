import random
print("Random floating numbers between 5 and 95: ")
for x in range(6):
	print(round(random.uniform(5,95),2))  #use round (,2) for having floating upto 2 decimals
						# similarly round (,x) for x floating decimals
