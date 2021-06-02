print("Enter a sequence of numbers seperated by comma: ")
list1 = [x for x in input().split(",")]
list2 = []

for i in list1:
	if int(i)%2 == 1:
		j =str(int(i)**2)
		list2.append(j)

print(",".join(list2))
