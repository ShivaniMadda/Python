list1 = []
for i in range(1000,3001):
	count = 0
	a=str(i)
	for j in a:
		if int(j)%2 == 0:
			count+=1
	if count == 4:
		list1.append(str(i))

print(",".join(list1))
