from chess_constants import PieceColor, GameCode
from utils import Board, Player

if __name__ == '__main__':
    board = Board()
    board.showBoard()
    player1 = Player(PieceColor.WHITE, board)
    player2 = Player(PieceColor.BLACK, board)

    while board.status == GameCode.PLAYING:
        print("Player 1's turn:\n")
        while player1.getCommand():
            pass

        print("Player 2's turn:")
        while player2.getCommand():
            pass
