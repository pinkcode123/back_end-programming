from sys import argv
fullname = argv[1:4]
middlename = argv[1]

for x in fullname:
    if len(fullname) < 2:
        print("please Enter middle name ")
        break
    elif len(fullname) < 1:
        print("please Enter your surname")
        break
    else:
        print(f'{argv[3]},{middlename} {argv[2]}')
        break


