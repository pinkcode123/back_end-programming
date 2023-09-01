data = {
    "Gentle":"admin2",
    "Ruth": "123abcd",
}
def validate_user(name, password):

    name = input("enter username ")
    password = input("password ")
    if name in data:
        if password == data[name]:
            print("access granted")
        else:
            print("access denied")
