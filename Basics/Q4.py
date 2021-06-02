#import math
#a = 4
#b = math.sqrt(a)
#print(b)

s=input("Enter an integer sequence seperated by comma: ")

list1 = list(s.split(","))

for i in range(0,len(list1)):
	list1[i] = int(list1[i])

C = 50
H = 30

for D in list1:
	if D != list1[len(list1)-1]:
		Q = int(((2*C*D)/H)**0.5)
		print(Q,end=",")
	else:
		Q = int(((2*C*D)/H)**0.5)
		print(Q)
