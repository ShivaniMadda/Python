n=int(input("Enter a nth number: "))
dict = {}
for i in range(1,n+1):
	key = i
	value = i*i
	dict[key] = value

print(dict)
