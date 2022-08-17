# type casting = convert the data type of a value to another data type

x = 6     #int
y = 6.9   #float
z = "3"   #string

print("int:",x)
print("float:",y)
print("string:",z*3)

print("")         # for asthetics

y = int(y)
z = int(z)

print("float to int:",y)
print("string to int:",z*3)    

print("")         # for asthetics

###################################

x = 6     #int
y = 6.9   #float
z = "3"   #string

x = float(y)
z = float(z)

print("int to float:",x)
print("string to float:",z*3)

print("")        # for asthetics

###################################

x = 6     #int
y = 6.9   #float
z = "3"   #string

x = str(x)
y = str(y)

print("int to string:",x)
print("float to string:",z*3)
