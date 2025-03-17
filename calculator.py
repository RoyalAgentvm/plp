def calculator():
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    sign=input('enter the sign to use: ')

    if sign == '+':
        value=num1 + num2
        print(num1, sign, num2, '=', value )
    elif sign == '-':
        value=num1 - num2
        print(num1, sign, num2, '=', value)
    elif sign == '*':
        value=num1 * num2
        print(num1, sign, num2, '=', value)
    elif sign == '/':
        value=num1 / num2
        print(num1, sign, num2, '=', value)
    

calculator()