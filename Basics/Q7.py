a = input("Enter a sequence of whitespace separated words: ")

set1 = set(a.split(" "))

list1 = list(set1)

list1.sort()

print(" ".join(list1))
