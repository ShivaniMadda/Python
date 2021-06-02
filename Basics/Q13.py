import re
value = []
items=[x for x in input().split(',')]
for i in items:
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[$#@]",i):
        continue
    elif re.search("\s",i):
        continue
    else:
        pass
    value.append(i)
print (",".join(value))
