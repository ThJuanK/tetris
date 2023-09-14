from enum import Enum

from functions.functions import *


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

points = 0
screen = new_screen = [["🔲"] * 10 for _ in range(10) ]
estadoRotacion = 0
actualPiece = Piece.S

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

def auto_down():
    global screen
    global estadoRotacion
    while screen != False:
        screen, estadoRotacion = move_piece(screen, Move.DOWN, estadoRotacion)
        time.sleep(2)
    
    t.cancel()

def tetris():
    global screen
    global estadoRotacion
    global actual_piece
    
    screen=generate_next_piece(screen)

    while screen != False:
        event = keyboard.read_event()
        if event.event_type == "down":
            match event.name:
                case "a" | "flecha izquierda" | "left": 
                    screen, estadoRotacion = move_piece(screen, Move.LEFT, estadoRotacion)
                case "s" | "flecha abajo" | "down": 
                    screen, estadoRotacion = move_piece(screen, Move.DOWN, estadoRotacion)
                case "d" | "flecha derecha" | "rigth": 
                    screen, estadoRotacion = move_piece(screen, Move.RIGTH, estadoRotacion)
                case "space": 
                    screen, estadoRotacion = move_piece(screen, Move.ROTATE, estadoRotacion)
                    
def game_over():
    global points
    system("cls")
    t.cancel()
    print(
       f"""
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬛⬛⬛⬛⬜⬜⬜⬛⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬜
        ⬜⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜
        ⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜
        ⬜⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜
        ⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜
        ⬜⬛⬛⬛⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ SCORE: {points}
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬜⬛⬜⬛⬛⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜
        ⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜
        ⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜
        ⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬛⬜⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        """
    )
    return False

def generate_next_piece(screen):
    
    global actualPiece
    global points
    
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
    
    actualPiece = Piece.I # random.choice(list(Piece))
                  
    for pixel in pieces[actualPiece]:
        
        if screen[i][j] == "⬛":
            return game_over()
        
        if pixel == 1:
            screen[i][j] = "🔳"
            
        if j == j_inicial + 2:
            j = j_inicial
            i += 1  
        else:
            j = j + 1
                      
    print_screen(screen, points)
    
    return screen

def move_piece(screen, move: Move, estadoRotacion: int = 0):
    global points
    
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
            
                if (((0 <= new_row_index <= 9)and( 0 <= new_column_index <= 9)) and not(new_screen[new_row_index][new_column_index] == "⬛")):
                    new_screen[new_row_index][new_column_index] = "🔳"
                    if new_row_index == len(screen) - 1 or new_screen[new_row_index + 1][new_column_index] == "⬛":
                        g_piece = True
                else:
                    return screen, estadoRotacion
    
    if g_piece:
        new_points = 0
        
        new_screen, new_points = piece_below(new_screen, points)
        points += new_points
        print(t.daemon)
        new_screen = generate_next_piece(new_screen)
        return new_screen, 0
    
    print_screen(new_screen, points)
    return new_screen, new_estadoRotacion


t = threading.Timer(interval=1, function=auto_down)
t.start()
tetris()    
