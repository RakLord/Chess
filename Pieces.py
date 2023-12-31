import Config
from Config import *


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.history = []
        self.legal_moves = []
        self.position = position
        self.symbol = (self.__class__.__name__[0] if color == 'b' else self.__class__.__name__[0].lower())

    def move(self, new_pos):
        old_pos = self.position
        self.history.append(old_pos)
        self.position = new_pos
        return old_pos, new_pos


    def get_legal_moves(self, board, position):
        pass

    def get_straight(self, board, position, diagonal=False):
        moves = []
        if diagonal:
            directions = [V2(1, 1), V2(1, -1), V2(-1, -1), V2(-1, 1)]  # DOWN-RIGHT, UP-RIGHT, UP-LEFT, DOWN-LEFT
        else:
            directions = [V2(0, 1), V2(0, -1), V2(-1, 0), V2(1, 0)]  # DOWN, UP, LEFT, RIGHT

        for _x, _y in directions:
            for distance in range(1, 8):
                new_location = V2(position.x + (_x * distance), position.y + (_y * distance))
                if 0 <= new_location.x < 8 and 0 <= new_location.y < 8:
                    ocupier = get_piece(board, new_location)
                    if ocupier is None:
                        moves.append(new_location)
                    elif ocupier.color != self.color:
                        moves.append(new_location)
                        break
                    else:
                        break
                else:
                    break

        # print("{} {}".format(self.symbol, moves))
        return moves


class Pawn(Piece):  # THIS IS FUCKED, I SHOULD PROBS CHANGE THE WAY I HANDLE X AND Y TO A VECTOR 2 LOL
    def get_legal_moves(self, board, position):
        self.legal_moves = []
        # direction = 1 if self.color == 'w' else -1
        #
        # if position[1] + direction < 8 and (board[position[1] + direction][position[0]]) is None:
        #     self.legal_moves.append((position[0], position[1] + direction))
        #     print(self.legal_moves)
        #     if not self.history:
        #         if 0 <= position[1] + 2 * direction < 8 and not board[position[1] + 2 * direction][position[0]]:
        #             self.legal_moves.append((position[0], position[1] + 2 * direction))

        # # Diagonal captures
        # for dx in [-1, 1]:
        #     new_x, new_y = position[0] + dx, position[1] + direction
        #     if 0 <= new_x < 8 and 0 <= new_y < 8:
        #         target_square = board[new_y][new_x]
        #         if target_square and target_square.color != self.color:
        #             self.legal_moves.append((new_x, new_y))




class Rook(Piece):
    def get_legal_moves(self, board, position):
        self.legal_moves = self.get_straight(board, position)


class Knight(Piece):
    def get_legal_moves(self, board, position):
        self.legal_moves = []
        # move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        # for offset in move_offsets:
        #     new_x, new_y = position[0] + offset[0], position[1] + offset[1]
        #     if 0 <= new_x < 8 and 0 <= new_y < 8:
        #         target_square = board[new_y][new_x]
        #         if not target_square or target_square.color != self.color:
        #             self.legal_moves.append((new_x, new_y))


class Bishop(Piece):
    def get_legal_moves(self, board, position):
        self.legal_moves = self.get_straight(board, position, diagonal=True)


class Queen(Piece):
    def get_legal_moves(self, board, position):
        self.legal_moves = self.get_straight(board, position) + self.get_straight(board, position, diagonal=True)


class King(Piece):
    def get_legal_moves(self, board, position):
        self.legal_moves = []
        # move_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # for offset in move_offsets:
        #     new_x, new_y = position[0] + offset[0], position[1] + offset[1]
        #     if 0 <= new_x < 8 and 0 <= new_y < 8:
        #         target_square = board[new_y][new_x]
        #         if not target_square or target_square.color != self.color:
        #             self.legal_moves.append((new_x, new_y))

