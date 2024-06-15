from typing import List

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


class Board:
    def __init__(self) -> None:
        self.BOARD: List[List[Piece | None]] = [[None] * GameCode.SIZE for _ in range(GameCode.SIZE)]
        self.status = GameCode.PLAYING
        self.BOARD[0][0] = Piece(0, 0, PieceColor.BLACK, PieceType.ROOK)
        self.BOARD[0][1] = Piece(0, 1, PieceColor.BLACK, PieceType.KNIGHT)
        self.BOARD[0][2] = Piece(0, 2, PieceColor.BLACK, PieceType.BISHOP)
        self.BOARD[0][3] = Piece(0, 3, PieceColor.BLACK, PieceType.QUEEN)
        self.BOARD[0][4] = Piece(0, 4, PieceColor.BLACK, PieceType.KING)
        self.BOARD[0][5] = Piece(0, 5, PieceColor.BLACK, PieceType.BISHOP)
        self.BOARD[0][6] = Piece(0, 6, PieceColor.BLACK, PieceType.KNIGHT)
        self.BOARD[0][7] = Piece(0, 7, PieceColor.BLACK, PieceType.ROOK)

        for i in range(SIZE):
            self.BOARD[1][i] = Piece(1, i, PieceColor.BLACK, PieceType.PAWN)

        self.BOARD[7][0] = Piece(0, 0, PieceColor.WHITE, PieceType.ROOK)
        self.BOARD[7][1] = Piece(0, 1, PieceColor.WHITE, PieceType.KNIGHT)
        self.BOARD[7][2] = Piece(0, 2, PieceColor.WHITE, PieceType.BISHOP)
        self.BOARD[7][3] = Piece(0, 3, PieceColor.WHITE, PieceType.QUEEN)
        self.BOARD[7][4] = Piece(0, 4, PieceColor.WHITE, PieceType.KING)
        self.BOARD[7][5] = Piece(0, 5, PieceColor.WHITE, PieceType.BISHOP)
        self.BOARD[7][6] = Piece(0, 6, PieceColor.WHITE, PieceType.KNIGHT)
        self.BOARD[7][7] = Piece(0, 7, PieceColor.WHITE, PieceType.ROOK)

        for i in range(SIZE):
            self.BOARD[6][i] = Piece(6, i, PieceColor.WHITE, PieceType.PAWN)

    def showBoard(self) -> None:
        print("*" * (SIZE + 3) * 2)
        for i in range(SIZE):
            print("** ", end="")
            for j in range(SIZE):
                if self.BOARD[i][j]:
                    print(self.BOARD[i][j].symbol + " ", end="")
                else:
                    print("  ", end="")
            # print("**")
            print()
        print("*" * (SIZE + 3) * 2)


class Player:
    def __init__(self, c: PieceColor, board: Board) -> None:
        self.color = c
        self.board = board

    def getCommand(self) -> int:
        """
        Codes are of the form:
        show [a-h][1-8]             # To show the moves available for the piece at that location
        move [chessNotation]        # To make the move represented
        """
        print(">>>", end=" ")
        cmd = input().split()

        if cmd[0] in "show":
            x = 8 - int(cmd[1][1])
            y = ord('a') - ord(cmd[1][0])
            self.showMoves(x, y)
            return 1

        if cmd[0] in "move":
            self.makeMove()
            return 0

        print("Invalid command entered")
        return -1

    def showMoves(self, x: int, y: int) -> None:
        pass

    def makeMove(self):
        pass
