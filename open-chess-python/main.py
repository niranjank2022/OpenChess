from typing import *

SIZE = 8
BOARD = [[None] * SIZE for _ in range(SIZE)]
WHITE = -1
BLACK = 1


class King:         # Idea to include castling moves?
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
        
    def nextMoves(self) -> List[Tuple]:
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not i == j == 0 and 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and BOARD[self.row + i][self.col + j]:
                    moves.append((i, j))
        
        return moves
    
class Queen:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c

    def nextMoves(self) -> List[Tuple]:
        moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == y == 0:
                    continue

                i, j = x, y
                while 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and not BOARD[self.row + i][self.col + j]:
                    moves.append((i, j))
                    i += x
                    j += y
        
        return moves

class Rook:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
    
    def nextMoves(self) -> List[Tuple]:
        moves = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = x, y
            while 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and not BOARD[self.row + i][self.col + j]:
                moves.append((i, j))
                i += x
                j += y
        

class Bishop:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
    
    def nextMoves(self) -> List[Tuple]:
        moves = []
        for x, y in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            i, j = x, y
            while 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and not BOARD[self.row + i][self.col + j]:
                moves.append((i, j))
                i += x
                j += y

class Knight:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
    
    def nextMoves(self) -> List[Tuple]:
        moves = []

        for i, j in [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]:
            if 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and BOARD[self.row + i][self.col + j]:
                moves.append((i, j))
        
        return moves

class Pawn:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
        self.notMoved = True
    
    def nextMoves(self) -> List[Tuple]:         # Idea about en passant and promotion?
        moves = []
        
        i = 1 * self.color
        if 0 <= self.row + i < SIZE and BOARD[self.row + i][self.col]:
            moves.append((i, 0))
        
        i = 2 * self.color
        if self.notMoved and 0 <= self.row + i < SIZE and BOARD[self.row + i][self.col]:
            moves.append((i, 0))
        
        i = self.color
        for j in [-1, 1]:
            if 0 <= self.col + j < SIZE and BOARD[self.row + i][self.col + j] and BOARD[self.row + i][self.col + j].color != self.color:
                moves.append((i, j))
        
        return moves
