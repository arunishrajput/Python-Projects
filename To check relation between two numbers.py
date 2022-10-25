# To check relation between two numbers (<),(>)&(=)

a = input('Enter A :')
b = input('Enter B :')

if a == b:
   print('The two numbers are equal')
elif a>b:                    # if first statement is false then second will run
    print('a is greater than b')
else:                        # if both statements are false then third statement will run
    print('b is greater than a')