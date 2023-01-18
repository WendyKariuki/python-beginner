astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print("first", istr)

istr = "Bob"

try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1
finally:
    print("the finally block runs regardless of any error")

a = 10
b = 0
try:
    print(a/b)
except:
    print("You cannot divide a number by zero")
finally:
    print("The end")

print("I've learnt about git today")