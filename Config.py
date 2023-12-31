import pygame as pg


class V2:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        return iter((self.x, self.y))


def get_piece(board, vector):
    piece = board[vector.y][vector.x]
    return piece
