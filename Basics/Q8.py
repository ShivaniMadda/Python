items = []
print("Enter sequence of 4-bit binary numbers seperated by comma:")
num = [x for x in input().split(",")]

for i in num:
	a = int(i,2)
	if not a%5 :
		items.append(i)

print(",".join(items))
