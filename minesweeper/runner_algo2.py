import pygame
import sys
import time

from algo2 import Minesweeper2, MinesweeperAI2

HEIGHT = 16
WIDTH = 16
MINES = 30
win_count = 0
loss_count = 0
start_time = time.time()
completed_games = 0


# Colors
CYAN = (87,210,185)
GRAY = (102,102,102)
WHITE = (255, 255, 255)
CYAN = (87,210,185)
RED = (255, 0, 0)

icon = pygame.image.load("minesweeper/2.png")
icon = pygame.transform.scale(icon, (300, 300)) 
# Create game
pygame.init()
size = width, height = 1000, 650
screen = pygame.display.set_mode(size)

# Fonts
OPEN_SANS = "minesweeper/assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 25)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 40)

# Compute board size
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
board_origin = (BOARD_PADDING, BOARD_PADDING)

# Add images
flag = pygame.image.load("minesweeper/assets/images/flag.png")
flag = pygame.transform.scale(flag, (cell_size, cell_size))
mine = pygame.image.load("minesweeper/assets/images/mine.png")
mine = pygame.transform.scale(mine, (cell_size, cell_size))
mine_red = pygame.image.load("minesweeper/assets/images/mine-red.png")
mine_red = pygame.transform.scale(mine_red, (cell_size, cell_size))

# Detonated mine
mine_detonated = None

# Create game and AI agent
game = Minesweeper2(height=HEIGHT, width=WIDTH, mines=MINES)
ai = MinesweeperAI2(height=HEIGHT, width=WIDTH)

# Keep track of revealed cells, flagged cells, and if a mine was hit
revealed = set()
flags = set()
lost = False

# Show instructions initially
instructions = True

# Autoplay game
autoplay = False
autoplaySpeed = 0.00001
makeAiMove = False

 
# Show Safe and Mine Cells
showInference = False
win_label = pygame.font.Font(OPEN_SANS, 20).render("Wins: 0", True, (255, 255, 255))
win_label_rect = win_label.get_rect()
win_label_rect.bottomright = (width - 150, height - 20)

loss_label = pygame.font.Font(OPEN_SANS, 20).render("Losses: 0", True, (255, 255, 255))
loss_label_rect = loss_label.get_rect()
loss_label_rect.bottomright = (width - 20, height - 20)
def update_counters():
    global win_label, win_label_rect, loss_label, loss_label_rect
    
    # Update win and loss counts
    win_label = pygame.font.Font(OPEN_SANS, 20).render(f"Wins: {win_count}", True, WHITE)
    win_label_rect = win_label.get_rect()
    win_label_rect.bottomright = (width - 150, height - 20)
    loss_label = pygame.font.Font(OPEN_SANS, 20).render(f"Losses: {loss_count}", True, WHITE)
    loss_label_rect = loss_label.get_rect()
    loss_label_rect.bottomright = (width - 20, height - 20)






while True:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# Calculate elapsed time
    if start_time is not None:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(f"Elapsed Time: {int(minutes)}:{int(seconds):02d}")
    screen.fill(CYAN)

    # Show game instructions
    if instructions:

        # Title
        title = largeFont.render("Play Minesweeper with Urchie", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Rules
        rules = [
            "Click a cell to reveal it.",
            "Right-click a cell to mark it as a mine.",
            "Mark all mines successfully to win!"
        ]
        for i, rule in enumerate(rules):
            line = smallFont.render(rule, True, WHITE)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 150 + 30 * i)
            screen.blit(line, lineRect)

        # Play game button
        buttonRect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 50)

        # Draw the icon near the start game button
        iconRect = icon.get_rect()
        iconRect.midbottom = (buttonRect.centerx, buttonRect.top - 1)
        screen.blit(icon, iconRect)

        buttonText = mediumFont.render("Play Game", True, CYAN)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = buttonRect.center
        pygame.draw.rect(screen, WHITE, buttonRect)
        screen.blit(buttonText, buttonTextRect)

        # Check if play button clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if buttonRect.collidepoint(mouse):
                instructions = False
                time.sleep(0.3)

        pygame.display.flip()
        continue

    # Draw board
    cells = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):

            # Draw rectangle for cell
            rect = pygame.Rect(
                board_origin[0] + j * cell_size,
                board_origin[1] + i * cell_size,
                cell_size, cell_size
            )
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, WHITE, rect, 3)

            # Add a mine, flag, or number if needed
            if game.is_mine((i, j)) and lost:
                if (i,j) == mine_detonated:
                    screen.blit(mine_red, rect)
                else:
                    screen.blit(mine, rect)
            elif (i, j) in flags:
                screen.blit(flag, rect)
            elif (i, j) in revealed:
                neighbors = smallFont.render(
                    str(game.nearby_mines((i, j))),
                    True, CYAN
                )
                neighborsTextRect = neighbors.get_rect()
                neighborsTextRect.center = rect.center
                screen.blit(neighbors, neighborsTextRect)
            elif (i, j) in ai.safes and showInference:
                pygame.draw.rect(screen, CYAN, rect)
                pygame.draw.rect(screen, WHITE, rect, 3)
            elif (i, j) in ai.mines and showInference:
                pygame.draw.rect(screen, RED, rect)
                pygame.draw.rect(screen, WHITE, rect, 3)
            row.append(rect)
        cells.append(row)

    # Autoplay Button
    autoplayBtn = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, BOARD_PADDING,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    bText = "Urchie" if not autoplay else "Stop"
    buttonText = mediumFont.render(bText, True, CYAN)
    buttonRect = buttonText.get_rect()
    buttonRect.center = autoplayBtn.center
    pygame.draw.rect(screen, WHITE, autoplayBtn)
    screen.blit(buttonText, buttonRect)

    # AI Move button
    aiButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, BOARD_PADDING + 70,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = mediumFont.render("AI Move", True, CYAN)
    buttonRect = buttonText.get_rect()
    buttonRect.center = aiButton.center
    if not autoplay:
        pygame.draw.rect(screen, WHITE, aiButton)
        screen.blit(buttonText, buttonRect)

    # Reset button
    resetButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, BOARD_PADDING + 140,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = mediumFont.render("Reset", True, CYAN)
    buttonRect = buttonText.get_rect()
    buttonRect.center = resetButton.center
    if not autoplay:
        pygame.draw.rect(screen, WHITE, resetButton)
        screen.blit(buttonText, buttonRect)

    # Display text
    text = "Lost" if lost else "Won" if game.mines == flags else ""
    text = mediumFont.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = ((5 / 6) * width, BOARD_PADDING + 232)
    screen.blit(text, textRect)

    # Show Safes and Mines button
    safesMinesButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, BOARD_PADDING + 280,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    bText = "Show Inference" if not showInference else "Hide Inference"
    buttonText = smallFont.render(bText, True, CYAN)
    buttonRect = buttonText.get_rect()
    buttonRect.center = safesMinesButton.center
    if not autoplay:
        pygame.draw.rect(screen, WHITE, safesMinesButton)
        screen.blit(buttonText, buttonRect)

    move = None

    left, _, right = pygame.mouse.get_pressed()

    # Check for a right-click to toggle flagging
    if right == 1 and not lost and not autoplay:
        mouse = pygame.mouse.get_pos()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if cells[i][j].collidepoint(mouse) and (i, j) not in revealed:
                    if (i, j) in flags:
                        flags.remove((i, j))
                    else:
                        flags.add((i, j))
                    time.sleep(0.2)

    elif left == 1:
        mouse = pygame.mouse.get_pos()

        # If Autoplay button clicked, toggle autoplay
        if autoplayBtn.collidepoint(mouse):
            if not lost:
                autoplay = not autoplay
            else:
                autoplay = False
            time.sleep(0.2)
            continue

        # If AI button clicked, make an AI move
        elif aiButton.collidepoint(mouse) and not lost:
            makeAiMove = True
            time.sleep(0.2)

        # Reset game state
        elif resetButton.collidepoint(mouse):
            game = Minesweeper2(height=HEIGHT, width=WIDTH, mines=MINES)
            ai = MinesweeperAI2(height=HEIGHT, width=WIDTH)
            revealed = set()
            flags = set()
            lost = False
            mine_detonated = None
            continue

        # If Inference button clicked, toggle showInference
        elif safesMinesButton.collidepoint(mouse):
            showInference = not showInference
            time.sleep(0.2)

        # User-made move
        elif not lost:
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if (cells[i][j].collidepoint(mouse)
                            and (i, j) not in flags
                            and (i, j) not in revealed):
                        move = (i, j)

    # If autoplay, make move with AI
    if autoplay or makeAiMove:
        if makeAiMove:
            makeAiMove = False
        move = ai.make_safe_move()
        if move is None:
            move = ai.make_random_move()
            if move is None:
                flags = ai.mines.copy()
                print("No moves left to make.")
                autoplay = False
            else:
                print("No known safe moves, AI making random move.")
        else:
            print("AI making safe move.")

        # Add delay for autoplay
        if autoplay:
            time.sleep(autoplaySpeed)

    # Make move and update AI knowledge
    if move:
        if game.is_mine(move):
            lost = True
            loss_count += 1
            completed_games += 1
            update_counters()
              # Increment loss count
            mine_detonated = move
    
            game = Minesweeper2(height=HEIGHT, width=WIDTH, mines=MINES)
            ai = MinesweeperAI2(height=HEIGHT, width=WIDTH)
            revealed = set()
            flags = set()
            lost = False
            mine_detonated = None
        else:
            nearby = game.nearby_mines(move)
            revealed.add(move)
            ai.add_knowledge(move, nearby)
            if len(revealed) == (HEIGHT * WIDTH) - MINES:
                # Game won
                win_count += 1 
                completed_games += 1 # Increment win count
                update_counters()  # Update counters
                time.sleep(1)
                game = Minesweeper2(height=HEIGHT, width=WIDTH, mines=MINES)
                ai = MinesweeperAI2(height=HEIGHT, width=WIDTH)
                revealed = set()
                flags = set()
                mine_detonated = None
                continue
            if completed_games >= 1000:
                print("Maximum number of completed games reached. Exiting.")
                print(f"Total Wins: {win_count}")
                print(f"Total Losses: {loss_count}")
                print(f"Total Games Played: {completed_games}")
                sys.exit()
            if move is not None and game.is_mine(move) and len(revealed) == 1:
                loss_count -= 1
                completed_games -= 1
                  # Decrement completed games
                print("Agent lost from the first random move. Not counting as a loss.")

    screen.blit(win_label, win_label_rect)
    screen.blit(loss_label, loss_label_rect)
    pygame.display.flip()

