def number_pattern(n):
    if not isinstance(n, int):
        print('Argument must be an integer value.')
    elif n < 1:
        print('Argument must be an integer greater than 0.')
    else:
        for patron in range(1, n+1):
            print(patron)
