data = {
    'Gentle': 'admin2',
    'Ruth' : '123abcd',
}


def validate_user(name, password):
    if name in data:
        if password == data[name]:
            return 'Yes'
        else:
            return 'No'
name =input("Enter your name : ")
password = input("enter password : ")
check = validate_user(name, password)
if check == "Yes":
    print("Acess granted")
else:
    print("Access denied")

