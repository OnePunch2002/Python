mystring = 'hello'
myfloat = 10.0
myint = 20

print('String : ', mystring)
print('Float : ', myfloat)
print('Int : ', myint)

print()

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    