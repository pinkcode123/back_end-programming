
def calc( numb1,numb3,):
    user_input = int(input("Enter a number $ "))
    for x in user_input:
        if user_input == "+":
            ans = numb1 + numb3
            print(f'the sum of {numb1} and {numb3} = {ans}')
calc()