mystring ="python is a cool program"
# converting mystring in to ascii character
binary="".join(format(ord(a),"b")for a in mystring)
print(binary)