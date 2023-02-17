

#Calculator

#Add
'''Add n1 and n2'''
def add(n1, n2):
    return n1 + n2

#Subtract
'''Subtract n1 - n2'''
def subtract(n1, n2):
    return n1 - n2

#Multiply
'''Multiply n1 * n2'''
def multiply(n1, n2):
    return n1*n2

#Divide
'''Divide n1 / n2'''
def divide(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Error, can't divide by 0"

operations = { '+':add, 
    '-':subtract, 
    "*": multiply, 
    '/': divide
}

from art import logo

def calculator():
    
    print(logo)

    num1 = float(input("First number "))
    for symbols in operations:
        print(symbols)
    should_continue = True #flag

    while should_continue:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("Second number "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if cont == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


    