from defs import *
import pygame, math, copy, helpers

#Auttaja funktiot
def xFromSquare(square):
    return square % COLUMNS

def yFromSquare(square):
    return math.floor(square/COLUMNS)

def squareFromXY(x, y):
    return x + y * COLUMNS

class moveGen:
    def __init__(self):
        self.moveList = []

    def slider(self, board, square : int, direction):
        x = xFromSquare(square)
        y = yFromSquare(square)
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
            x += xmod
            y += ymod
            piece = board.getPieceOnCord(x, y)
            if piece == EMPTY_PIECE:
                return Move(-1, 0, 0, EMPTY_PIECE)
            if piece == board.getActivePlayer():
                if steps > 1:
                    return Move(square, steps, xmod + ymod * COLUMNS, board.getActivePlayer())
                return Move(-1, 0, 0, EMPTY_PIECE)

    def generate(self, board):
        for i in range(N_SQUARES):
            if (board.getPieceOnSquare(i) == EMPTY_PIECE):
                #Jos ruutu on tyhja, tarkista onko siirto ruutuun mahdollinen tarkistamalla eri suunnassa olevat nappulat.
                for dir in range(DIRECTIONS):
                    m = self.slider(board, i, dir)
                    if m.steps > 0:
                        self.moveList.append(m)
                    
#Siirto luokka
class Move:
    def __init__(self, start, steps, direction, color):
        self.start     = start
        self.steps     = steps
        self.direction = direction
        self.color     = color

def evaluate(board):
    PSTScore = 0
    for i in range(N_SQUARES):
        PSTScore += board.getPieceOnSquare(i) * (PST[i] + 50)
    return PSTScore * board.getActivePlayer()

def Negamax(depth, ply, board, alpha, beta):
    if depth == 0:
        return evaluate(board)
    score = -10**11
    mGen = moveGen()
    mGen.generate(board)
    bestMove = -1
    for move in mGen.moveList:
        newBoard = copy.deepcopy(board)
        newBoard.makeMove(move)
        newScore = -Negamax(depth - 1, ply + 1, newBoard, -beta, -alpha)
        if newScore > score:
            score = newScore
            bestMove = move
        alpha = max(score, alpha)
        if alpha >= beta:
            return alpha
    if ply == 0:
        board.bestMove = bestMove
    return score

#Laudan luokka
class Board:
    
    def __init__(self):
        self.__pieceList     = [0] * N_SQUARES;
        self.__pieceList[D4] = BLACK_PIECE
        self.__pieceList[E4] = WHITE_PIECE
        self.__pieceList[D5] = WHITE_PIECE
        self.__pieceList[E5] = BLACK_PIECE
        self.__activePlayer  = WHITE_PIECE
        self.bestMove        = 0 #temp value set by Negamax

    def setPiece(self, square, piece):
        self.__pieceList[square] = piece

    def getPieceOnSquare(self, square):
        if square < 0 or square >= N_SQUARES:
            return 0
        return self.__pieceList[square]

    def getPieceOnCord(self, x, y):
        if x >= COLUMNS or x < 0 or y >= ROWS or y < 0:
            return 0
        return self.__pieceList[y * ROWS + x]

    def getActivePlayer(self):
        return self.__activePlayer

    def makeMove(self, move : Move):
        # We asume that the move is legal
        for i in range(move.steps):
            self.__pieceList[move.start + i * move.direction] = move.color
        self.__activePlayer = 0 - move.color

    def isWin(self):
        mGen = moveGen()
        mGen.generate(self)
        if len(mGen.moveList) == 0:
            self.__activePlayer = 0 - self.__activePlayer
            mGen = moveGen()
            mGen.generate(self)
            if len(mGen.moveList) == 0:
                score = 0
                for i in range(N_SQUARES):
                    score += self.getPieceOnSquare(i)
                return 2 + max(-1, min(1, score))
            return ONGOING
        return ONGOING

    def render(self, screen):
        #piirra tausta
        pygame.draw.rect(screen, GREEN, (X_OFFSET, Y_OFFSET, CELL_SIZE * COLUMNS, CELL_SIZE * ROWS))

        #Piirra ruudukko
        for i in range(COLUMNS + 1):
            pygame.draw.line(screen, DARK_GREEN, (X_OFFSET,  Y_OFFSET + CELL_SIZE * i), (X_OFFSET + CELL_SIZE * COLUMNS,  Y_OFFSET + CELL_SIZE * i), 5)
            pygame.draw.line(screen, DARK_GREEN, (X_OFFSET + CELL_SIZE * i, Y_OFFSET), (X_OFFSET + CELL_SIZE * i, Y_OFFSET + CELL_SIZE * ROWS), 5)

        #Piirra siirtovuoronappula
        if self.__activePlayer == WHITE_PIECE:
            pygame.draw.circle(screen, WHITE, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)
        else: 
            pygame.draw.circle(screen, BLACK, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)

        for x in range (COLUMNS):
            for y in range (ROWS):
                if self.__pieceList[y * COLUMNS + x] == 0:
                    pass
                elif self.__pieceList[y * COLUMNS + x] == WHITE_PIECE:
                    pygame.draw.circle(screen, WHITE, (X_OFFSET + x * CELL_SIZE + CELL_SIZE / 2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)
                elif self.__pieceList[y * COLUMNS + x] == BLACK_PIECE:
                    pygame.draw.circle(screen, BLACK, (X_OFFSET + x * CELL_SIZE + CELL_SIZE / 2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)

        winState = self.isWin()
        helpers.drawButton(screen, WIN_X, WIN_Y, WINSTATES[winState], helpers.cursorOnTextBox(WIN_X, WIN_Y, WINSTATES[winState], BUTTON_FONT))

    def tick(self, screen, events, loader):
        self.render(screen)

        helpers.drawButton(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, helpers.cursorOnTextBox(ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT))
        helpers.drawButton(screen, SAVE_X, SAVE_Y, SAVE_T, helpers.cursorOnTextBox(SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT))
        helpers.drawButton(screen, NEW_X, NEW_Y, NEW_T, helpers.cursorOnTextBox(NEW_X, NEW_Y, NEW_T, BUTTON_FONT))
        helpers.drawButton(screen, LOAD_X, LOAD_Y, LOAD_T, helpers.cursorOnTextBox(LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cord = pygame.mouse.get_pos()
                x = cord[0]
                y = cord[1]
                lautaX = math.floor((x-X_OFFSET)/CELL_SIZE)
                lautaY = math.floor((y-Y_OFFSET)/CELL_SIZE)
                if not (lautaX >= COLUMNS or lautaX < 0 or lautaY >= ROWS or lautaY < 0):
                    mGen = moveGen()
                    mGen.generate(self)
                    for move in mGen.moveList:
                        if move.start == squareFromXY(lautaX, lautaY):
                            self.makeMove(move)
                if helpers.cursorOnTextBox(ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT):
                    Negamax(5, 0, self, -10**20, 10**20)
                    if self.bestMove != -1:
                        self.makeMove(self.bestMove)

                if helpers.cursorOnTextBox(NEW_X, NEW_Y, NEW_T, BUTTON_FONT):
                    self.__init__()
                
                if helpers.cursorOnTextBox(SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT):
                    loader.add(self)