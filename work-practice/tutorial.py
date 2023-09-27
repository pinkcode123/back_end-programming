numbers = int(input("Enter a number $ "))
stopvalue = int(input("Enter a number $ "))
interval = int(input("Enter a interval $ "))
arithmetic = (input("Enter an arithmetor +,-,x $ "))
for x in range(1, stopvalue + 1, interval):
    if arithmetic == "+":
        ans = numbers + x
        print(f"{numbers} + {x} = {ans}")
    elif arithmetic == "-":
        ans = numbers - x
        print(f"{numbers} - {x} = {ans}")
    elif arithmetic == "x":
        ans = numbers * x
        print(f"{numbers} x {x} = {ans}")
