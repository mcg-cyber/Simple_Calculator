# Purpose: Just for fun
# Author: mcg-cyber
import sys


def main():
    while True:
        try:
            """ Simple Calculator """
            print('Here you can choose what calculation you want to make.'
                  '\n1. Add'
                  '\n2. Subtract'
                  '\n3. Multiply'
                  '\n4. Divide')
            op = input("Enter your choice: ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op == '1':
                print(num1 + num2)
                again()
            elif op == '2':
                print(num1 - num2)
                again()
            elif op == '3':
                print(num1 * num2)
                again()
            elif op == '4':
                print(num1 / num2)
                again()
        except ValueError as error:
            print(f"Invalid input {error}")


def again():
    ask = input("Calculate again? (y/n)")
    if ask == 'y':
        main()
    else:
        print("Ok. Bye!")
        sys.exit(0)


if __name__ == '__main__':
    main()
