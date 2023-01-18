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
