def hexacode():
    user_input = input("Write some stuff $  ")
    converter = "".join(format(ord(a), "b")for a in user_input)
    print(converter)


hexacode()