from enum import Enum
from os import system
import keyboard
import threading
import time
import random

class Piece(Enum):
    I = 0
    S = 1
    L = 2
    J = 3
    O = 4
    Z = 5
    T = 6

class Move(Enum):
    LEFT = 0
    RIGTH = 1
    DOWN = 2
    ROTATE = 3
    UP = 4

screen = new_screen = [["🔲"] * 10 for _ in range(10) ]
estadoRotacion = 0
actualPiece = Piece.S

def auto_down():
    global screen
    global estadoRotacion
    while True:
        screen, estadoRotacion = move_piece(screen, Move.DOWN, estadoRotacion)
        time.sleep(2)

def tetris():
    global screen
    global estadoRotacion
    global actual_piece
    
    screen=generate_next_piece(screen)

    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            match event.name:
                case "a" | "flecha izquierda": 
                    screen, estadoRotacion = move_piece(screen, Move.LEFT, estadoRotacion)
                case "s" | "down": 
                    screen, estadoRotacion = move_piece(screen, Move.DOWN, estadoRotacion)
                case "d" | "rigth": 
                    screen, estadoRotacion = move_piece(screen, Move.RIGTH, estadoRotacion)
                case "space" | "left": 
                    screen, estadoRotacion = move_piece(screen, Move.ROTATE, estadoRotacion)
                    

def piece_below(screen):
    for row_index_2, row_2 in enumerate(screen):
        for column_index_2, pixel_2 in enumerate(row_2):
            if pixel_2 == "🔳":
                screen[row_index_2][column_index_2] = "⬛"
                
    return screen

# lista de modificaciones por pixel de cada pieza
rotaciones = {
    Piece.I: [
        [(0, 0), (-1 , 1), (-2, 2)],
        [(2, 2), (1 , 1), (0, 0)],
        [(2, -2), (1 , -1), (0, 0)],
        [(-2, 0), (-1 , -1), (0, -2)],
    ],
    Piece.O: [
        [(0, 0), (0 , 0), (0, 0), (0, 0)] for _ in range(4)
    ],
    Piece.S: [
        [(1, -1), (0 , -2), (1, 1), (0, 0)],
        [(1, 0), (0 , 1), (-1, 0), (-2, 1)],              
        [(1, -1), (0 , -2), (1, 1), (0, 0)],           
        [(1, 0), (0 , 1), (-1, 0), (-2, 1)],                
    ],
    Piece.Z: [
        [(0, 1), (1, 0), (0, -1), (1, -2)],     
        [(1, 1), (-1 , 1), (0, 0), (-2, 0)],               
        [(0, 1), (1, 0), (0, -1), (1, -2)],     
        [(1, 1), (-1 , 1), (0, 0), (-2, 0)],               
    ],
    Piece.Z: [
        [(0, 1), (1, 0), (0, -1), (1, -2)],
        [(1, 1), (-1 , 1), (0, 0), (-2, 0)],
        [(0, 1), (1, 0), (0, -1), (1, -2)],
        [(1, 1), (-1 , 1), (0, 0), (-2, 0)],
    ],
    Piece.J: [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)], 
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)],
    ],
    Piece.L: [
        [(1, 1), (0, 0), (-1, -1), (0, -2)],
        [(0, 1), (1, 0), (2, -1), (-1, 0)],
        [(0, 1), (1, 0), (0, -1), (-1, -2)],
        [(2, 0), (-1, 1), (0, 0), (1, -1)],
    ],
    Piece.T: [
        [(1, 1), (-1, 1), (0, 0), (1, -1)],
        [(1, 1), (0, 0), (1, -1), (-1, -1)],
        [(-1, 1), (0, 0), (1, -1), (-1, -1)],
        [(1, 1), (-1, 1), (0, 0), (-1, -1)],
    ]
}

def generate_next_piece(screen):
    
    global actualPiece
    
    pieces = {
        Piece.I: 
        [1, 0, 0,
         1, 0, 0,
         1, 0, 0], # I
        Piece.O:
        [1, 1, 0, 
         1, 1, 0,
         0, 0, 0], # O
        Piece.S:
        [0, 1, 1,
         1, 1, 0,
         0, 0, 0], # S
        Piece.Z:
        [1, 1, 0,
         0, 1, 1,
         0, 0, 0], # Z
        Piece.J:
        [0, 1, 0,
         0, 1, 0,
         1, 1, 0], # J
        Piece.L:
        [0, 1, 0,
         0, 1, 0,
         0, 1, 1], # L
        Piece.T:
        [0, 1, 0,
         1, 1, 1,
         0, 0, 0], # T
    }
    
    j_inicial = random.randint(0, 7)
    j = j_inicial
    i = 0
    
    actualPiece = random.choice(list(Piece))
                  
    for pixel in pieces[actualPiece]:
        print(f"{i}, {j} \n{pixel} \n")

        print_screen(screen, False)
        
        if pixel == 1:
            screen[i][j] = "🔳"
            
        if j == j_inicial + 2:
            j = j_inicial
            i += 1  
        else:
            j = j + 1
                      
    print_screen(screen)
    
    return screen

def print_screen(screen, clean = True):
    if clean:
        system('cls')
    for row in screen:
        print( "".join( map( str, row ) ),)
    print("\n")

def move_piece(screen, move: Move, estadoRotacion: int = 0):
    new_screen = [["🔲"] * 10 for _ in range(10) ]
    
    for row_index, row in enumerate(screen):
        for column_index, pixel in enumerate(row):
            if pixel == "⬛":
                new_screen[row_index][column_index] = "⬛"
    
    g_piece = False
         
    n_pieza = 0
    new_estadoRotacion = estadoRotacion
    
    if move == Move.ROTATE:
        new_estadoRotacion = 0 if estadoRotacion == 3 else estadoRotacion + 1
    
    for row_index, row in enumerate(screen):
        for column_index, pixel in enumerate(row):
            new_row_index = 0
            new_column_index = 0
            
            
            if pixel == "🔳":
                
                match move:
                    case Move.RIGTH:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                        
                    case Move.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                        
                    case Move.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index 
                        
                    case Move.UP:
                        new_row_index = row_index - 1
                        new_column_index = column_index 
                        
                    case Move.ROTATE:
                        new_row_index = row_index + rotaciones[actualPiece][estadoRotacion][n_pieza][0]
                        new_column_index =  column_index  + rotaciones[actualPiece][estadoRotacion][n_pieza][1]
                        n_pieza += 1
            
                if ((0 <= new_row_index <= 9) and ( 0 <= new_column_index <= 9)):
                    new_screen[new_row_index][new_column_index] = "🔳"
                    if new_row_index == len(screen) - 1 or new_screen[new_row_index + 1][new_column_index] == "⬛":
                        new_screen = piece_below(new_screen)
                        g_piece = True
                else:
                    return screen, estadoRotacion
    
    if g_piece:
        new_screen = generate_next_piece(new_screen)
        return new_screen, 0
    
    print_screen(new_screen)
    return new_screen, new_estadoRotacion
    
t = threading.Timer(interval=3, function=auto_down)
t.start()
tetris()
