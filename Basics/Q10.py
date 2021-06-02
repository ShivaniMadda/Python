s = input("Enter a sentence containing letters, numbers and special characters: ")
alpha = ""
num = ""
special = ""

for i in range(len(s)):
	if (s[i].isdigit()):
		num += s[i]
	elif (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z"):
		alpha += s[i]
	else:
		special += s[i]

print("Letters: ",len(alpha))
print("Digits: ",len(num))
print("Special characters: ",len(special))

