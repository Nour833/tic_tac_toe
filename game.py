from random import randint as ri

struct = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
for i in range(9):
    def cal(char):
        progress = False
        xnum = 0
        for i in range(3):
            xnum += struct[i].count(char)
        if xnum >= 3:
            num = 0
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


    while (i % 2) == 0:
        inp = input("""
                                                      x
                                                      
                                                  1   2   3                                  
                                                +---+---+---+
                                           1    | {0} | {1} | {2} |
                                                +---+---+---+
                                    y      2    | {3} | {4} | {5} |
                                                +---+---+---+
                                           3    | {6} | {7} | {8} |
                                                +---+---+---+
                                      
                                      type for example 12 (1 y and 2 x)  
                                      =======> """.format(struct[0][0], struct[0][1], struct[0][2], struct[1][0],
                                                          struct[1][1],
                                                          struct[1][2], struct[2][0], struct[2][1], struct[2][2]))
        try:
            int(inp)
        except:
            continue
        if len(inp) == 2 and ((1 <= int(inp[0]) <= 3) and (1 <= int(inp[1]) <= 3) and len(inp) == 2) and (
                struct[int(inp[0]) - 1][int(inp[1]) - 1] == " "):
            break
    if (i % 2) == 0:
        char = "x"
    else:
        char = "O"
    if char == "x":
        struct[int(inp[0]) - 1][int(inp[1]) - 1] = char
    else:
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
        if ((struct[0][0] == "x" and struct[2][2] == "x") or (struct[0][2] == "x" and struct[2][0] == "x")) and (
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
    if cal("x"):
        print("X WINS ¯\_(ツ)_/¯ !!!!!")
        break
    elif cal("O"):
        print("""
                                                      x
                                                      
                                                  1   2   3                                  
                                                +---+---+---+
                                           1    | {0} | {1} | {2} |
                                                +---+---+---+
                                    y      2    | {3} | {4} | {5} |
                                                +---+---+---+
                                           3    | {6} | {7} | {8} |
                                                +---+---+---+
                                      O WINS ¯\_(ツ)_/¯ !!!!!
                                      """.format(struct[0][0], struct[0][1], struct[0][2], struct[1][0],
                                                 struct[1][1],
                                                 struct[1][2], struct[2][0], struct[2][1], struct[2][2]))
        break
