mylist = [2, 1, 'this', 4, '10', (3, 2), 'fun', 'python']


def new_list(value):
    string = []
    alphabet = []
    integer = []
    for x in value:
        if isinstance(x, int):
            integer.append(x)
    print(integer)

    for x in value:
        if isinstance(x, str):
            string.append(x)
    print(string)
    for character in string:
        if character.isalpha():
            alphabet.append(character)
    print(alphabet)
    print("Invalid option")


new_list(mylist)

