def draw_rectangle(height, width, symbol):
    for i in range (height):
        for j in range (width):
            print(symbol, end='')
        print('')
draw_rectangle(4, 5, '*')
