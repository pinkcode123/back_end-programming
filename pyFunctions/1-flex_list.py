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
        if isinstance(x,str):
            string.append(x)
    print(string)
    for x in string:
        if x.isalpha():
            alphabet.append(x)
    print(alphabet)

new_list(mylist)