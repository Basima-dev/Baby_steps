# This is a calculator program
#The input section
print('Welcome to the calculator!')
print('enter your first number')
x = int(input('>'))
print('enter operator type')
y = input('>')
print('enter the second number')
z = int(input('>'))

# The condition section
for v in y:
    if y == "+":
        ans = x + z
    elif y == "-":
        ans = x-z
    elif y == "*":
        ans = x*z
        print(__annotations__)
    elif y == "/":
        ans = x/z
    else:
        print('invalid operator')
        
# The answer section   
print(x, y, z, '=', ans)


