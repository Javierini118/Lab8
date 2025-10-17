import pygame
import random
from piece import Piece

ROWS, COLS = 20, 10
CELL_SIZE = 30

# Colores de piezas
COLORS = [
    (0, 255, 255),   # I
    (0, 0, 255),     # J
    (255, 165, 0),   # L
    (255, 255, 0),   # O
    (0, 255, 0),     # S
    (128, 0, 128),   # T
    (255, 0, 0)      # Z
]

# Formas (matrices 0/1)
SHAPES = [
    [[1, 1, 1, 1]],                      # I
    [[1, 0, 0], [1, 1, 1]],              # J
    [[0, 0, 1], [1, 1, 1]],              # L
    [[1, 1], [1, 1]],                    # O
    [[0, 1, 1], [1, 1, 0]],              # S
    [[0, 1, 0], [1, 1, 1]],              # T
    [[1, 1, 0], [0, 1, 1]]               # Z
]

class Board:
    """Lógica del tablero de Tetris (simplificada para laboratorio)."""
    def __init__(self, width, height):
        self.grid = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]
        self.current_piece = self.new_piece()
        self.width = width
        self.height = height
        self.gravity_counter = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        return Piece(shape, color)

    def move_piece(self, dx):
        self.current_piece.x += dx
        if not self.valid_position():
            self.current_piece.x -= dx

    def drop_piece(self):
        self.current_piece.y += 1
        if not self.valid_position():
            self.current_piece.y -= 1
            self.lock_piece()

    def tick_gravity(self):
        # hace caer la pieza cada cierto número de frames
        self.gravity_counter += 1
        if self.gravity_counter >= 10:
            self.gravity_counter = 0
            self.drop_piece()

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, val in enumerate(row):
                if val:
                    gy = self.current_piece.y + y
                    gx = self.current_piece.x + x
                    if 0 <= gy < ROWS and 0 <= gx < COLS:
                        self.grid[gy][gx] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.new_piece()
        # si la pieza nueva nace ocupada, juego sobre
        if not self.valid_position():
            self.reset()

    def reset(self):
        # Reinicia el tablero (comportamiento simple para no cerrar el juego)
        self.grid = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]

    def clear_lines(self):
        # Conserva filas que aún tienen celdas vacías; elimina las llenas.
        self.grid = [row for row in self.grid if (0, 0, 0) in row]
        while len(self.grid) < ROWS:
            self.grid.insert(0, [(0, 0, 0) for _ in range(COLS)])

    def valid_position(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, val in enumerate(row):
                if val:
                    px = self.current_piece.x + x
                    py = self.current_piece.y + y
                    if px < 0 or px >= COLS or py >= ROWS:
                        return False
                    if py >= 0 and self.grid[py][px] != (0, 0, 0):
                        return False
        return True

    def draw(self, win):
        # Dibujar celdas fijas
        for y in range(ROWS):
            for x in range(COLS):
                pygame.draw.rect(
                    win, self.grid[y][x],
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
                )
        # Dibujar la pieza actual
        self.current_piece.draw(win)
