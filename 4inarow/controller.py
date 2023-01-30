import sys
import pygame

# Constants
ROW = 6
COL = 7
WIDTH = 100
HEIGHT = 100
MARGIN = 10
RADIUS = int(WIDTH / 2 - 5)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (0, 0, 255)
ANIMATION_SPEED = 5
FPS = 60
# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode(((WIDTH + MARGIN) * COL + MARGIN, (HEIGHT + MARGIN) * ROW + MARGIN))
pygame.display.set_caption("4 in a Row, it's red's turn")
clock = pygame.time.Clock()

# The board represented as a 2D list
board = [[0 for _ in range(COL)] for _ in range(ROW)]


def is_valid_move(col):
    return board[ROW - 1][col] == 0


def all_full():
    for col in range(COL):
        if board[ROW-1][col] == 0:
            return False
    return True


def get_next_open_row(col):
    for row in range(ROW):
        if board[row][col] == 0:
            return row


def drop_disc(row, col, player):
    board[row][col] = player


def draw_disc(row, col, color):
    pygame.draw.circle(screen, color, (
        int((col + 0.5) * WIDTH + (col + 1) * MARGIN), int((row + 0.5) * HEIGHT + (row + 1) * MARGIN)), RADIUS)


def draw_board():
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 1:
                color = RED
                draw_disc(row, col, color)
            elif board[row][col] == -1:
                color = YELLOW
                draw_disc(row, col, color)
            else:
                color = [255, 255, 255]
            pygame.draw.circle(screen, color,
                               [(MARGIN + WIDTH) * col + MARGIN + 50, (MARGIN + HEIGHT) * row + MARGIN + 50], RADIUS)


def check_for_win(row, col):
    # Check horizontal
    count = 0
    for i in range(COL):
        if board[row][i] == board[row][col]:
            count += 1
        else:
            count = 0
        if count == 4:
            return True

    # Check vertical
    count = 0
    for i in range(ROW):
        if board[i][col] == board[row][col]:
            count += 1
        else:
            count = 0
        if count == 4:
            return True

    # Check positive diagonal
    count = 0
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == board[row][col]:
            count += 1
        else:
            break
    for i, j in zip(range(row + 1, ROW), range(col + 1, COL)):
        if board[i][j] == board[row][col]:
            count += 1
        else:
            break
        if count == 4:
            return True

    # Check negative diagonal
    count = 0
    for i, j in zip(range(row, -1, -1), range(col, COL)):
        if board[i][j] == board[row][col]:
            count += 1
        else:
            break
        for i, j in zip(range(row + 1, ROW), range(col - 1, -1, -1)):
            if board[i][j] == board[row][col]:
                count += 1
            else:
                break
        if count == 4:
            return True


def animate_disc(row, col, color):
    y = HEIGHT * ROW + MARGIN
    while y > (row * HEIGHT + (row + 1) * MARGIN):
        y -= ANIMATION_SPEED
        screen.fill(BACKGROUND_COLOR)
        draw_board()
        draw_disc(int((y - MARGIN) / HEIGHT), col, color)
        pygame.display.update()
        clock.tick(FPS)
    draw_disc(row, col, color)
