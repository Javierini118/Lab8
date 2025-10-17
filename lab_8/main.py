import pygame
from board import Board

# Inicializar pygame
pygame.init()
WIDTH, HEIGHT = 300, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Simple - lab_8")

clock = pygame.time.Clock()
FPS = 10

def main():
    board = Board(WIDTH, HEIGHT)
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            board.move_piece(-1)
        if keys[pygame.K_RIGHT]:
            board.move_piece(1)
        if keys[pygame.K_DOWN]:
            board.drop_piece()

        # caída automática
        board.tick_gravity()

        # dibujar
        win.fill((20, 20, 20))
        board.draw(win)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
