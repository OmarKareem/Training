var1 = int (input("enter first number"))
var2 = int (input("enter second number"))
operator = input("plus , multiply , devide, minus")

if operator == 'plus':
    print(var1 + var2)
elif operator == 'multiply':
    print( var1 * var2)
elif operator == 'devide':
    print(var1 / var2)
elif operator == 'minus':
    print(var1 - var2)
else:
    print("you entered the wrong number")