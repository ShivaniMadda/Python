list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list3=['0','1','2','3','4','5','6','7','8','9']
list4=['@','#','$']


print("Enter a sequence of passwords seperated by comma: ")
a=input()
lst1= list(a.split(","))
lst2=[]

for i in lst1:
	if len(i)>6 and len(i)<12 and " " not in i:
		count1 = 0
		count2 = 0
		count3 = 0
		count4 = 0
		for j in i:
			if j in list1:
				count1 += 1
			elif j in list2:
				count2 += 1
			elif j in list3:
				count3 += 1
			elif j in list4:
				count4 += 1
		if count1 >=1 and count2 >=1 and count3 >=1 and count4 >=1:
			lst2.append(i)

print(",".join(lst2))
