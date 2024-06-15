from chess_constants import *


class Piece:
    def __init__(self, x: int, y: int, c: PieceColor, piece_type: PieceType) -> None:
        self.row = x
        self.col = y
        self.color = c
        self.type = piece_type

        match self.type:
            case PieceType.KING:
                self.symbol = '♔' if self.color == PieceColor.WHITE else '♚'
            case PieceType.QUEEN:
                self.symbol = '♕' if self.color == PieceColor.WHITE else '♛'
            case PieceType.ROOK:
                self.symbol = '♖' if self.color == PieceColor.WHITE else '♜'
            case PieceType.BISHOP:
                self.symbol = '♗' if self.color == PieceColor.WHITE else '♝'
            case PieceType.KNIGHT:
                self.symbol = '♘' if self.color == PieceColor.WHITE else '♞'
            case PieceType.PAWN:
                self.symbol = '♙' if self.color == PieceColor.WHITE else '♟'

"""
    
class King:         # Idea to include castling moves?
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
        self.symbol = '♔' if self.color == WHITE else '♚'
        
    def nextMoves(self, board: List[List[King | Queen | Rook | Bishop | Knight | Pawn | None ]]) -> List[Tuple]:
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not i == j == 0 and 0 <= self.row + i < SIZE and 0 <= self.col + j < SIZE and board[self.row + i][self.col + j]:
                    moves.append((i, j))
        
        return moves
    
class Queen:
    def __init__(self, x: int, y: int, c: int) -> None:
        self.row = x
        self.col = y
        self.color = c
        self.symbol = '♕' if self.color == WHITE else '♛'

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
        self.symbol = '♖' if self.color == WHITE else '♜'
    
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
        self.symbol = '♗' if self.color == WHITE else '♝'
    
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
        self.symbol = '♘' if self.color == WHITE else '♞'

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
        self.symbol = '♙' if self.color == WHITE else '♟︎'
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

"""
