while True:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    h = int(input('Third number: '))
    if a <= b:
        for a in range(a, b+1, h):
            print(a)
        break
    else:
        print('Error! Invalid number! Try again.')
