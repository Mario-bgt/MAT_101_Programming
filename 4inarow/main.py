from controller import *

"""
This code implements a 4 in a row game in Python using the Pygame library. The game has a graphical user 
interface, where the user can place the discs by clicking on columns. When a disc is placed, it will animate as it 
falls into the first available row in the selected column. The game checks for a win after every move and stops when 
there is a winning combination of 4 discs of the same color in a row, either horizontally, vertically, or diagonally. 

The game uses a 2D list board to represent the state of the game, where each element in the list is either 1 for 
player 1's disc, -1 for player 2's disc, or 0 for an empty space. The game logic, such as checking for a valid move, 
getting the next open row, and checking for a win, is implemented in separate functions, making the code easy to 
understand and maintain. The Pygame library is used to draw the game board, discs, and handle user input. 

Overall, the code is well-structured, using functions and variables with descriptive names to make the code easy to 
understand and modify. The animation of the falling discs adds a fun and engaging element to the game, making it a 
great project for learning more about game development in Python and Pygame. 

This code was mainly developed by artificial intelligence and then further adjusted by me.
"""

player = 1
game_over = False

# Main game loop
while not game_over:
    if all_full():
        player = 0
        game_over = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if player == 1:
                    pygame.display.set_caption("4 in a Row, it's yellow's turn")
                else:
                    pygame.display.set_caption("4 in a Row, it's red's turn")
                col = int(event.pos[0] // (WIDTH + MARGIN))
                if is_valid_move(col):
                    row = get_next_open_row(col)
                    animate_disc(row, col, RED if player == 1 else YELLOW)
                    drop_disc(row, col, player)
                    if check_for_win(row, col):
                        game_over = True
                    player *= -1
                else:
                    font = pygame.font.Font(None, 72)
                    text = font.render("This colum is already full!", True, GREEN)
                    screen.blit(text, [100, 100])
                    pygame.display.flip()
                    pygame.time.wait(1000)
    screen.fill(BACKGROUND_COLOR)
    draw_board()
    pygame.display.update()
    clock.tick(FPS)

# Game over
font = pygame.font.Font(None, 72)
if player == 1:
    text = font.render("Yellow wins!", True, YELLOW)
elif player == 0:
    text = font.render("It's a tie!", True, GREEN)
else:
    text = font.render("Red wins!", True, RED)
text_rect = text.get_rect()
text_x = screen.get_width() / 2 - text_rect.width / 2
text_y = screen.get_height() / 2 - text_rect.height / 2
screen.blit(text, [text_x, text_y])
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
