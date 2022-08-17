# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "pen chor"             # order for indexing->  [start:stop:step]

first_name = name[:3]         # [:3] and [0:3] same thing
last_name  = name[4:8]
shet_name = name[::2]         # if stop index is empty, python will assume last part of the string as end/stop point
shetty_name = name[:8:3]

print(first_name)
print(last_name)
print(shet_name)
print(shetty_name)
print()


# reverse a name
x = "batman"
y = x[::-1]
print("reversed name: ",y)
print()


# slicing
# order for slicing->  slice(start,stop,step)

website1 = "http://google.com"
website2 = "http://youtube.com"
z = slice(7,-4)       # using -ve index will count from right to left
print(website1[z])
print(website2[z])