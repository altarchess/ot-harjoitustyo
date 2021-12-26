import pygame


"""
Ohjelmassa kaytettavien vakioiden maaritelmat       
"""

# Tiedosto jonne othello asemat tallennetaan
SAVE_FILE = "saved.othello"

# Kayttoliittyman moodit
PLAY = 1
LOAD = 2
SETTINGS = 3

# Naytto
WIDTH = 500
HEIGHT = 550

# Luadalle tarkeita
N_SQUARES = 64
COLUMNS = 8
ROWS = 8
WHITE_PIECE = 1
BLACK_PIECE = -1
EMPTY_PIECE = 0

# Laudan grafiikkaa
X_OFFSET = 10
Y_OFFSET = 60
CELL_SIZE = 60
PIECE_SIZE = 25

# Asetukset
AI_LEVEL = "AI level"
SHOW_LEGAL = "Show legal moves"

# Napit ja muu grafiikka
pygame.init()
BUTTON_FONT = pygame.font.SysFont(None, 25)
ENGINE_MOVE_X = X_OFFSET
ENGINE_MOVE_Y = X_OFFSET
ENGINE_MOVE_T = "AI move"
SAVE_X = X_OFFSET + 90
SAVE_Y = X_OFFSET
SAVE_T = "Save"
NEW_X = X_OFFSET + 150
NEW_Y = X_OFFSET
NEW_T = "New"
LOAD_X = X_OFFSET + 205
LOAD_Y = X_OFFSET
LOAD_T = "Load"
WIN_X = X_OFFSET + 360
WIN_Y = X_OFFSET
OPTIONS_X = X_OFFSET + 260
OPTIONS_Y = X_OFFSET
OPTIONS_T = "Options"
OPTIONS_Y_OFFSET = 50
PREVIOUS_X = X_OFFSET
PREVIOUS_Y = X_OFFSET
PREVIOUS_T = "Previous"
NEXT_X = X_OFFSET + 125
NEXT_Y = X_OFFSET
NEXT_T = "Next"

# Kordinaatit
A1 = 0
B1 = 1
C1 = 2
D1 = 3
E1 = 4
F1 = 5
G1 = 6
H1 = 7

A2 = 8
B2 = 9
C2 = 10
D2 = 11
E2 = 12
F2 = 13
G2 = 14
H2 = 15

A3 = 16
B3 = 17
C3 = 18
D3 = 19
E3 = 20
F3 = 21
G3 = 22
H3 = 23

A4 = 24
B4 = 25
C4 = 26
D4 = 27
E4 = 28
F4 = 29
G4 = 30
H4 = 31

A5 = 32
B5 = 33
C5 = 34
D5 = 35
E5 = 36
F5 = 37
G5 = 38
H5 = 39

A6 = 40
B6 = 41
C6 = 42
D6 = 43
E6 = 44
F6 = 45
G6 = 46
H6 = 47

A7 = 48
B7 = 49
C7 = 50
D7 = 51
E7 = 52
F7 = 53
G7 = 54
H7 = 55

A8 = 56
B8 = 57
C8 = 58
D8 = 59
E8 = 60
F8 = 61
G8 = 62
H8 = 63

# Move directions
DIRECTIONS = 8
N = 0
NE = 1
E = 2
SE = 3
S = 4
SW = 5
W = 6
NW = 7

# Varit
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
DARK_GREEN = (0, 100, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# Pelin lopputulos
WHITE_WIN = 3
BLACK_WIN = 1
DRAW = 2
ONGOING = 0
WINSTATES = ["In progress", "Black wins", "Draw", "White wins"]

# Evaluation
PST = [100,     -15,    15,     5,      5,      15,     -15,    100,
       -15,     -25,    -5,     -5,     -5,     -5,     -25,    -15,
       15,      -5,     10,     5,      5,      10,     -5,     15,
       5,       -5,     5,      5,      5,      5,      -5,     5,
       5,       -5,     5,      5,      5,      5,      -5,     5,
       15,      -5,     10,     5,      5,      10,     -5,     15,
       -15,     -25,    -5,     -5,     -5,     -5,     -25,    -15,
       100,     -15,    15,     5,      5,      15,     -15,    100]
