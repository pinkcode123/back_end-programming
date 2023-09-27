import cmd
from os import system

class Calc(cmd.Cmd):
    prompt = "Calculator$ "


    def do_pt(self, args):
        """The pt is use to print users input just like the echo statement in linux print in python"""
        print(args)

    def do_cal(self, args):
        """this function will add users input"""
        values = args.split()
        num1 = int(values[0])
        sign = values[1]
        num2 = int(values[2])
        if sign == "+":
            print(num1 + num2)
        elif sign == '-':
            print(num1 - num2)

    def do_clear(self, args):
        """clear the screenn"""
        system('cls')

if __name__ == '__main__':
    Calc().cmdloop()