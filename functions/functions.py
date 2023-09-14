from os import system
import time

def print_screen(screen, points, clean = True):
    if clean:
        system('cls')
    for i, row in enumerate(screen):
        print( "".join( map( str, row ) if i != 3 else f"{''.join( map( str, row ))}  score: {points}"),) 
    print("\n")
    
def clean_row(screen, row_index, points):
    
    for x in range(10):
        screen[row_index][x] = "🔲"
        print_screen(screen, points)
    
    screen.pop(row_index)
    screen.insert(0, ["🔲"]*10)
    
    time.sleep(0.5)
    print_screen(screen, points)
    
    return screen

def piece_below(screen, points):
    contador_de_lineas = 0
    points = 0
    
    for row_index, row in enumerate(screen):
        for column_index, pixel in enumerate(row):
            if pixel == "🔳":
                screen[row_index][column_index] = "⬛"
    
    for row_index, row in enumerate(screen):
        if all(pixel == "⬛" for pixel in row):
            contador_de_lineas += 1
            screen = clean_row(screen, row_index, points)
    
    match contador_de_lineas:
        case 1 | 2: points = 100 * contador_de_lineas
        case 3: points = 400
    
    return screen, points