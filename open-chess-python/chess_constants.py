from enum import Enum, IntEnum


class GameCode(IntEnum):
    SIZE = 8
    PLAYING = 0b01000000
    OVER = 0b10000000


class PieceColor(Enum):
    WHITE = -1
    BLACK = -2


class PieceType(Enum):
    KING = 0b00000001
    QUEEN = 0b00000010
    ROOK = 0b00000100
    BISHOP = 0b00001000
    KNIGHT = 0b00010000
    PAWN = 0b00100000
