import Config
from Config import *
from Pieces import *


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.initialize_board()

    @staticmethod
    def create_board():
        size = 8
        return [[None for _ in range(size)] for _ in range(size)]

    def initialize_board(self):
        self.board[0] = [Rook('b', V2(0, 0)), Knight('b', V2(0, 1)), Bishop('b', V2(0, 2)), Queen('b', V2(0, 3)),
                         King('b', V2(0, 4)), Bishop('b', V2(0, 5)), Knight('b', V2(0, 6)), Rook('b', V2(0, 7))]

        # self.board[1] = [Pawn('b', V2(1, i)) for i in range(8)]
        # Gap
        self.board[6] = [Pawn('w', V2(6, i)) for i in range(8)]
        self.board[7] = [Rook('w', V2(7, 0)), Knight('w', V2(7, 1)), Bishop('w', V2(7, 2)), Queen('w', V2(7, 3)),
                         King('w', V2(7, 4)), Bishop('w', V2(7, 5)), Knight('w', V2(7, 6)), Rook('w', V2(7, 7))]

    def print_board(self):
        for row in self.board:
            for col in row:
                if col is not None:
                    print(col.symbol, end=" ")
                elif col is None:
                    print(".", end=" ")

            print("")
        # for row in self.board:
        #     print(' '.join([piece.symbol if piece else '.' for piece in row]))

    def update_board(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece:
                    piece.get_legal_moves(self.board, V2(x, y))
                    # print("{}: {}".format(piece.symbol, piece.legal_moves))

    def move_piece(self, piece, new_pos):
        piece.move(self.board, new_pos)
        print(piece.__dict__)



chess_board = ChessBoard()
chess_board.print_board()
chess_board.update_board()

bishop1 = get_piece(chess_board.board, V2(2, 0))            # Select Bishop

chess_board.move_piece(bishop1, bishop1.legal_moves[0])     # Move Bishop
chess_board.update_board()                                  # Update Board
chess_board.print_board()

chess_board.move_piece(bishop1, bishop1.legal_moves[0])     # Move Bishop
chess_board.update_board()                                  # Update Board
chess_board.print_board()

chess_board.move_piece(bishop1, bishop1.legal_moves[0])     # Move Bishop
chess_board.update_board()                                  # Update Board
chess_board.print_board()

# print(get_piece(chess_board.board, V2(3, 3)))
