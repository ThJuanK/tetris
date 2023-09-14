from os import system
import time

def print_screen(screen, clean = True):
    if clean:
        system('cls')
    for row in screen:
        print( "".join( map( str, row ) ),)
    print("\n")
    
def clean_row(screen, row_index):
    print(row_index)
    for x in range(10):
        screen[row_index][x] = "🔲"
        print_screen(screen)
    
    screen.pop(9)
    screen.insert(0, ["🔲"]*10)
    
    time.sleep(0.5)
    print_screen(screen)
    
    return screen

def piece_below(screen):
    for row_index, row in enumerate(screen):
        for column_index, pixel in enumerate(row):
            if pixel == "🔳":
                screen[row_index][column_index] = "⬛"
    
    for row_index, row in enumerate(screen):
        if all(pixel == "⬛" for pixel in row):
            screen = clean_row(screen, row_index)
      
    return screen