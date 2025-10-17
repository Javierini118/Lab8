import pygame

CELL_SIZE = 30

class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        # Posición inicial aproximada centrada
        self.x = 3
        self.y = 0

    def draw(self, win):
        for y, row in enumerate(self.shape):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        win,
                        self.color,
                        ((self.x + x) * CELL_SIZE, (self.y + y) * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
                    )
