import entity.internal_board
from misc.defs import *


class MoveGen:

    """
    Siirtogeneraattoria hallitseva luokka.

    Attributes:
        move_list: Lista siirroista

    """

    def __init__(self):
        """
        Luodaan lista siirtoja varten. Tahan listaan generaattori sitten kirjoittaa generoidut siirrot
        """

        self.move_list = []

    def slider(self, board, square, direction):
        """
        Yrittaa generoida siirron tiettyyn suuntaan mahdollisesta kandidaattisiirtoruudusta.

        Args: 
            board: othello-lauta objekti jonka asemaan sirtoja halutaan generoida
            square: kandidaattiruutu josta siirtoja halutaan generoida
            direction: suunta johon on tarkoitus yritää siirtojen generoimista

        Returns:
            Palautta Move objektin, jossa siirron aloitusruutu on -1 jos siirtoa ei voida generoida,
            muuten siirron aloitusruutu on sama kuin argumenttina anettu.
        """

        square_x = entity.internal_board.x_from_square(square)
        square_y = entity.internal_board.y_from_square(square)
        xmod = 0
        ymod = 0

        if direction in (NW, N, NE):
            ymod += 1
        if direction in (SW, S, SE):
            ymod -= 1
        if direction in (NE, E, SE):
            xmod += 1
        if direction in (NW, W, SW):
            xmod -= 1

        steps = 0
        while True:
            steps += 1
            square_x += xmod
            square_y += ymod
            piece = board.get_piece_on_cord(square_x, square_y)
            if piece == EMPTY_PIECE:
                return Move(-1, 0, 0, EMPTY_PIECE)
            if piece == board.get_active_player():
                if steps > 1:
                    return Move(square, steps, xmod + ymod * COLUMNS, board.get_active_player())
                return Move(-1, 0, 0, EMPTY_PIECE)

    def generate(self, board):
        """
        Kokeilee kaikkia mahdollisia siirtoja, ja jos slider-funktio palauttaa siirron mahdollisena,
        lisataan se listaan.
        """

        for i in range(N_SQUARES):
            if (board.get_piece_on_square(i) == EMPTY_PIECE):
                for dir in range(DIRECTIONS):
                    m = self.slider(board, i, dir)
                    if m.steps > 0:
                        self.move_list.append(m)


class Move:

    """
    Luokka joka kuvaa yksittaista siirtoa
    """

    def __init__(self, start, steps, direction, color):
        self.start = start
        self.steps = steps
        self.direction = direction
        self.color = color
