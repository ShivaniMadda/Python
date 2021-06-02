s = input("Enter a sentence containing letters and special characters: ")
alpha_U = ""
alpha_L = ""
special = ""

for i in range(len(s)):
	if (s[i] >= "a" and s[i] <= "z"):
		alpha_L += s[i]
	elif (s[i] >= "A" and s[i] <= "Z"):
		alpha_U += s[i]
	else:
		special += s[i]

print("Upper Case: ",len(alpha_U))
print("Lower Case: ",len(alpha_L))
print("Special characters: ",len(special))


