
def calc(numb1, sign, numb2):
    user_input = int(input("Enter a number $ "))
    if user_input == "+":
        ans = numb1 + numb2
        print(f'the sum of {numb1}  {sign} and {numb2} = {ans}')
