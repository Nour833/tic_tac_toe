from random import randint as ri
import pygame, sys

struct = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
pygame.init()
WIDTH = HEIGHT = 600
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe (press R to restart)')
screen.fill(BG_COLOR)


def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def cal(char):
    progress = False
    xnum = 0
    for i in range(3):
        xnum += struct[i].count(char)
    if xnum >= 3:
        for i in range(3):
            num = struct[i].count(char)
            if num == 3:
                progress = True
                break
            else:
                num = struct[0][i].count(char) + struct[1][i].count(char) + struct[2][i].count(char)
                if num == 3:
                    progress = True
                    break
                else:
                    num = struct[0][0].count(char) + struct[1][1].count(char) + struct[2][2].count(char)
                    if num == 3:
                        progress = True
                        break
                    else:
                        num = struct[0][2].count(char) + struct[1][1].count(char) + struct[2][0].count(char)
                        if num == 3:
                            progress = True
                            break
    return progress


def avail(y, x):
    if struct[y][x] == " ":
        return True
    else:
        return False


def draw_fig():
    for row in range(3):
        for col in range(3):
            if struct[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif struct[row][col] == "x":
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


def check_win(player):
    for col in range(3):
        if struct[0][col] == player and struct[1][col] == player and struct[2][col] == player:
            ver_win(col, player)
            return True
    for row in range(3):
        if struct[row][0] == player and struct[row][1] == player and struct[row][2] == player:
            hor_win(row, player)
            return True
    if struct[2][2] == struct[0][0] == struct[1][1] == player:
        desc_win(player)
        return True
    if struct[2][0] == struct[0][2] == struct[1][1] == player:
        asc_win(player)
        return True
    return False


def ver_win(col, player):
    posX = col * 200 + 100
    if player == "x":
        color = CROSS_COLOR
    elif player == "O":
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def hor_win(row, player):
    posY = row * 200 + 100
    if player == "x":
        color = CROSS_COLOR
    elif player == "O":
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def asc_win(player):
    if player == "x":
        color = CROSS_COLOR
    elif player == "O":
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def desc_win(player):
    if player == "x":
        color = CROSS_COLOR
    elif player == "O":
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for r in range(3):
        for c in range(3):
            struct[r][c] = " "


number = 0
draw_lines()
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_y = int(mouseY // 200)
            clicked_x = int(mouseX // 200)
            if avail(clicked_y, clicked_x):
                struct[clicked_y][clicked_x] = "x"
                number += 1
                print(number)
                if check_win("x"):
                    game_over = True
                elif not check_win("x") and number < 9:
                    char = "O"
                    danger_y = danger_x = []
                    for i in range(3):
                        y_x = int(struct[i].count("x"))
                        y_o = int(struct[i].count("O"))
                        x_x = int(struct[0][i].count("x") + struct[1][i].count("x") + struct[2][i].count("x"))
                        x_o = int(struct[0][i].count("O") + struct[1][i].count("O") + struct[2][i].count("O"))
                        if (y_x == 2) and (y_o < 1):
                            danger_y = [i]
                            break
                        elif (x_x == 2) and (x_o < 1):
                            danger_x = [i]
                            break
                    if ((struct[0][0] == "x" and struct[2][2] == "x") or (
                            struct[0][2] == "x" and struct[2][0] == "x")) and (
                            struct[1][1] == " "):
                        struct[1][1] = char
                    elif struct[0][0] == " " and struct[1][1] == struct[2][2] == "x":
                        struct[0][0] = char
                    elif struct[2][0] == " " and struct[1][1] == struct[0][2] == "x":
                        struct[2][0] = char
                    elif struct[0][2] == " " and struct[1][1] == struct[2][0] == "x":
                        struct[0][2] = char
                    elif struct[2][2] == " " and struct[1][1] == struct[0][0] == "x":
                        struct[2][2] = char
                    elif len(danger_y) != 0:
                        y = danger_y[0]
                        num = struct[y].count("x")
                        index = [i for i, x in enumerate(struct[y]) if x == "x"]
                        middle = (index[0] + index[1]) / 2
                        if middle.is_integer():
                            struct[y][int(middle)] = char
                        elif 0 not in index:
                            struct[y][0] = char
                        elif 1 not in index:
                            struct[y][1] = char
                        elif 2 not in index:
                            struct[y][2] = char
                    elif len(danger_x) != 0:
                        x = danger_x[0]
                        num = struct[x].count("x")
                        index = []
                        for i in range(3):
                            numb = struct[i][x].count("x")
                            if numb != 0:
                                index.append(i)
                        middle = (index[0] + index[1]) / 2
                        if middle.is_integer():
                            struct[int(middle)][x] = char
                        elif 0 not in index:
                            struct[0][x] = char
                        elif 1 not in index:
                            struct[1][x] = char
                        elif 2 not in index:
                            struct[2][x] = char
                    else:
                        while True:
                            one = str(ri(1, 3))
                            two = str(ri(1, 3))
                            full = one + two
                            if struct[int(full[0]) - 1][int(full[1]) - 1] == " ":
                                break
                        struct[int(full[0]) - 1][int(full[1]) - 1] = char
                    number += 1
                    if check_win("O"):
                        game_over = True
                draw_fig()
            print(number)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                number = 0
                game_over = False
    pygame.display.update()
