from functools import reduce

# filter() with lambda()
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
final_list1 = list(filter(lambda x: (x%2 != 0) , list1))
print("Filtered: ")
print(final_list1)

# map() with lambda()
# to get double of a list.
final_list2 = list(map(lambda x: x*2 , list1))
print("Mapped: ")
print(final_list2)

#from functools import reduce
# reduce() with lambda()
# to get sum of a list
sum = reduce((lambda x, y: x + y), list1)
print("Reduced: ")
print (sum)
