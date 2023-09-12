mylist = [2, 1, 'this', 4, '10', (3, 2), 'fun']
num = []
for a in mylist:
    if isinstance(a, int):
        num.append(a)
print(num)
