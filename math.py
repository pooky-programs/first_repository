def add(integer1, integer2):
    value = integer1 + integer2
    return value


# using try: except: finally: for practice here!

try:
    print('-----------------------------------------')
    print('| hello! welcome to addition simulator. |')
    print('-----------------------------------------')
    print('please input two numbers.\n')

    user_input1 = int(input('enter first number: '))

    user_input2 = int(input('enter second number: '))

    print('result: ', add(user_input1, user_input2))
    print('wow! much calculation, good job')
except ValueError as error:
    print('\noh no! looks like the calculation failed: ', str(error))
finally:
    print('\nthank you for using addition simulator! goodbye.')