a=5
b=3
print("Before swapping:")
print("a=",a)   
print("b=",b)
#method1
# a,b=b,a
# print("a=",a)   
# print("b=",b)
#method2

a=a+b
b=a-b
a=a-b
print("After swapping:")
print("a=",a)   
print("b=",b)