
ls=['a',1,2]
l=[]
while(True):
	a=input("enter name: ")
	b=int(input("enter age: "))
	c=int(input("enter score: "))
	ls[0]=a
	ls[1]=b
	ls[2]=c
	t=tuple(ls)
	l.append(t)
	if('n'==input("n or y: ")):
		break



l.sort(key=lambda lst:lst[2],reverse=True)

l.sort(key=lambda lt:lt[1],reverse=True)

l.sort(key=lambda t:t[0])
print(l)

