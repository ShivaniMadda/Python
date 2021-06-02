# Multiline user input method 1
#n = 5
#lines = ""
#for i in range(5):
#	lines = lines + input() + "\n"
#print(lines)


# Multiline user input method 2
#lines = []
#while True:
#	line = input()
#	if line:
#		lines.append(line)
#	else:
#		break
#text = "\n".join(lines)
#print(text)


list1 = []
while True:
	line = input()
	if line:
		list1.append(line)
	else:
		break

text = "\n".join(list1)

print(text.upper())
