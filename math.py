def add(integer1, integer2):
    value = integer1 + integer2
    return value


def sub(integer1, integer2):
    value = integer1 - integer2
    return value


def menu():
    print()
    print('would you like to:')
    print('1. add\n2. subtract\n3. end program\n')


# using try: except: finally: for practice here!
try:
    prompt = True
    print('-------------------------------------')
    print('| hello! welcome to math simulator. |')
    print('-------------------------------------')

    while prompt:
        menu()
        command = int(input('please enter a command: '))
        print()

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
        elif command == 3:
            break

    print('wow! much calculation, good job')

except ValueError as error:
    print('\noh no! looks like the program or calculation failed: ', str(error))

finally:
    print('\nthank you for using math simulator! goodbye.')
