mystring = "python is a cool program, python is love, python is fun"
# Count the number of times 'python' repeats in the string
python = mystring.count("python")
print(python)

# Capitalize all characters in the string
capitalize = mystring.upper()
print(capitalize)

# Capitalize only the word 'python'
only = mystring.split()  # Split the string into words
capitalized_only = []
for word in only:
    if word == "python":
        capitalized_only.append(word.upper())
    else:
        capitalized_only.append(word)
capitalized_python = " ".join(capitalized_only)
print(capitalized_python)
