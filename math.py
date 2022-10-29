def add(integer1, integer2):
    value = integer1 + integer2
    return value


def sub(integer1, integer2):
    value = integer1 - integer2
    return value


def menu():
    print('would you like to:')
    print('1. add\n2. subtract')


# using try: except: finally: for practice here!
try:
    prompt = True
    print('-----------------------------------------')
    print('| hello! welcome to math simulator. |')
    print('-----------------------------------------')

    while prompt:
        command = input('please enter a command: ')

        if command == 1:
            print('please input two numbers.\n')
            user_input1 = int(input('enter first number: '))
            user_input2 = int(input('enter second number: '))
            print('result: ', add(user_input1, user_input2))

        elif command == 2:
            print('please input two numbers.\n')
            user_input1 = int(input('enter first number: '))
            user_input2 = int(input('enter second number: '))
            print('result: ', sub(user_input1, user_input2))

    print('wow! much calculation, good job')

except ValueError as error:
    print('\noh no! looks like the calculation failed: ', str(error))

finally:
    print('\nthank you for using math simulator! goodbye.')
