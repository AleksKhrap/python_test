while True:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    h = int(input('Third number: '))
    if a >= b:
        for i in range(a, b-1, -h):
            print(i)
        break
    else:
        print('Error! Invalid number! Try again.')
