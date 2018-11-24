# 2048 GUI
from graphics import *
from button import *
from tile import *
from random import *

def main():
    win = GraphWin("2048", 900, 700)
    tile_list = GUI(win)
    score = 0
    score_text = Text(Point(750, 152), score)
    score_text.setSize(36)
    score_text.setStyle("bold")
    score_text.setFace("times roman")
    score_text.draw(win)

# Buttons
    up_button = Button(win, Point(750, 250), 80, 50, "UP")
    down_button = Button(win, Point(750, 370), 80, 50, "DOWN")
    right_button = Button(win, Point(830, 310), 80, 50, "RIGHT")
    left_button = Button(win, Point(670, 310), 80, 50, "LEFT")
    restart_button = Button(win, Point(750, 470), 80, 50, "RESTART")
    quit_button = Button(win, Point(750, 550), 80, 50, "QUIT")
    up_button.activate()
    down_button.activate()
    right_button.activate()
    left_button.activate()
    restart_button.activate()
    quit_button.activate()

    for i in range(2):
        spawn_tile(win, tile_list)
        
    pt = win.getMouse()

    while not quit_button.clicked(pt):
        points_added = 0
        moved = False
        if restart_button.clicked(pt):
            win.close()
            main()
        elif up_button.clicked(pt):
            points_added, moved = move_up(win, tile_list)
        elif down_button.clicked(pt):
            points_added, moved = move_down(win, tile_list)
        elif right_button.clicked(pt):
            points_added, moved = move_right(win, tile_list)
        elif left_button.clicked(pt):
            points_added, moved = move_left(win, tile_list)
            
        score += points_added
        score_text.undraw()
        score_text = update_score(win, score)
        
        if moved == True:
            spawn_tile(win, tile_list)
            
        pt = win.getMouse()
    win.close()

def update_score(win, score):
    score_text = Text(Point(750, 152), score)
    score_text.setStyle("bold")
    score_text.setFace("times roman")
    score_text.setSize(36)
    score_text.draw(win)
    return score_text

def GUI(win):
    tile_list = [ ]
    for i in range(4):
        sub_tile_list = [ ]
        for k in range(4):
            center = Point(325 / 2 + 125 * i, 325 / 2 + 125 * k)
            fill = "white"
            label = 0
            row = i
            column = k
            new_square = Tile(win, center, fill, label, row, column)
            sub_tile_list.append(new_square)
        tile_list.append(sub_tile_list)
            

    score_rectangle = Rectangle(Point(675, 100), Point(825, 175))
    score_rectangle.setWidth("2")
    score_rectangle.setFill("honeydew")
    score_rectangle.draw(win)
    score_text = Text(Point(750, 118), "SCORE")
    score_text.setSize(20)
    score_text.setFace("times roman")
    score_text.draw(win)

    return tile_list

def spawn_tile(win, tile_list):
    rand_value = randint(0, 3)
    if rand_value == 0:
        square_value = 4
    else:
        square_value = 2
    success = False
    while success == False:
        index_one = randint(0, 3)
        index_two = randint(0, 3)
        if tile_list[index_one][index_two].getEmpty() == True:
            tile_list[index_one][index_two].changeLabel(square_value)
            tile_list[index_one][index_two].changeText(win)
            tile_list[index_one][index_two].fillSquare()
            tile_list[index_one][index_two].updateFill()
            success = True

def move_up(win, tile_list):
    points_added = 0
    moved = False
    for c in range(4):
        while tile_list[c][0].getEmpty() == True:
            if tile_list[c][1].getEmpty() == False:
                tile_list[c][0].changeLabel(tile_list[c][1].getLabel())
                tile_list[c][1].changeLabel(tile_list[c][2].getLabel())
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            elif tile_list[c][2].getEmpty() == False:
                tile_list[c][1].changeLabel(tile_list[c][2].getLabel())
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            elif tile_list[c][3].getEmpty() == False:
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)
        while tile_list[c][1].getEmpty() == True:
            if tile_list[c][2].getEmpty() == False:
                tile_list[c][1].changeLabel(tile_list[c][2].getLabel())
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            elif tile_list[c][3].getEmpty() == False:
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)
        while tile_list[c][2].getEmpty() == True:
            if tile_list[c][3].getEmpty() == False:
                tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
                tile_list[c][3].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)

        if tile_list[c][0].getLabel() == tile_list[c][1].getLabel():
            tile_list[c][0].doubleLabel()
            tile_list[c][1].changeLabel(tile_list[c][2].getLabel())
            tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
            tile_list[c][3].changeLabel(0)
            moved = True
            points_added += tile_list[c][0].getLabel()
        if tile_list[c][1].getLabel() == tile_list[c][2].getLabel():
            tile_list[c][1].doubleLabel()
            tile_list[c][2].changeLabel(tile_list[c][3].getLabel())
            tile_list[c][3].changeLabel(0)
            moved = True
            points_added += tile_list[c][1].getLabel()
        if tile_list[c][2].getLabel() == tile_list[c][3].getLabel():
            tile_list[c][2].doubleLabel()
            tile_list[c][3].changeLabel(0)
            moved = True
            points_added += tile_list[c][2].getLabel()
        up_and_down_check(c, tile_list)
        
        for tile in tile_list[c]:
            tile.changeText(win)
            tile.updateFill()

    return points_added, moved

def move_down(win, tile_list):
    points_added = 0
    moved = False
    for c in range(4):
        while tile_list[c][3].getEmpty() == True:
            if tile_list[c][2].getEmpty() == False:
                tile_list[c][3].changeLabel(tile_list[c][2].getLabel())
                tile_list[c][2].changeLabel(tile_list[c][1].getLabel())
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            elif tile_list[c][1].getEmpty() == False:
                tile_list[c][2].changeLabel(tile_list[c][1].getLabel())
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            elif tile_list[c][0].getEmpty() == False:
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)
        while tile_list[c][2].getEmpty() == True:
            if tile_list[c][1].getEmpty() == False:
                tile_list[c][2].changeLabel(tile_list[c][1].getLabel())
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            elif tile_list[c][0].getEmpty() == False:
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)
        while tile_list[c][1].getEmpty() == True:
            if tile_list[c][0].getEmpty() == False:
                tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
                tile_list[c][0].changeLabel(0)
                moved = True
            else:
                break
            up_and_down_check(c, tile_list)

        if tile_list[c][3].getLabel() == tile_list[c][2].getLabel():
            tile_list[c][3].doubleLabel()
            tile_list[c][2].changeLabel(tile_list[c][1].getLabel())
            tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
            tile_list[c][0].changeLabel(0)
            moved = True
            points_added += tile_list[c][3].getLabel()
        if tile_list[c][2].getLabel() == tile_list[c][1].getLabel():
            tile_list[c][2].doubleLabel()
            tile_list[c][1].changeLabel(tile_list[c][0].getLabel())
            tile_list[c][0].changeLabel(0)
            moved = True
            points_added += tile_list[c][2].getLabel()
        if tile_list[c][1].getLabel() == tile_list[c][0].getLabel():
            tile_list[c][1].doubleLabel()
            tile_list[c][0].changeLabel(0)
            moved = True
            points_added += tile_list[c][1].getLabel()
        up_and_down_check(c, tile_list)
        
        for tile in tile_list[c]:
            tile.changeText(win)
            tile.updateFill()
    
    return points_added, moved

def move_right(win, tile_list):
    points_added = 0
    moved = False
    for r in range(4):
        while tile_list[3][r].getEmpty() == True:
            if tile_list[2][r].getEmpty() == False:
                tile_list[3][r].changeLabel(tile_list[2][r].getLabel())
                tile_list[2][r].changeLabel(tile_list[1][r].getLabel())
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            elif tile_list[1][r].getEmpty() == False:
                tile_list[2][r].changeLabel(tile_list[1][r].getLabel())
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            elif tile_list[0][r].getEmpty() == False:
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            else:
                break
            right_and_left_check(r, tile_list)
        while tile_list[2][r].getEmpty() == True:
            if tile_list[1][r].getEmpty() == False:
                tile_list[2][r].changeLabel(tile_list[1][r].getLabel())
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            elif tile_list[0][r].getEmpty() == False:
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            else:
                break
            right_and_left_check(r, tile_list)
        while tile_list[1][r].getEmpty() == True:
            if tile_list[0][r].getEmpty() == False:
                tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
                tile_list[0][r].changeLabel(0)
                moved = True
            else:
                break
            right_and_left_check(r, tile_list)

        if tile_list[3][r].getLabel() == tile_list[2][r].getLabel():
            tile_list[3][r].doubleLabel()
            tile_list[2][r].changeLabel(tile_list[1][r].getLabel())
            tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
            tile_list[0][r].changeLabel(0)
            moved = True
            points_added += tile_list[3][r].getLabel()
        if tile_list[2][r].getLabel() == tile_list[1][r].getLabel():
            tile_list[2][r].doubleLabel()
            tile_list[1][r].changeLabel(tile_list[0][r].getLabel())
            tile_list[0][r].changeLabel(0)
            moved = True
            points_added += tile_list[2][r].getLabel()
        if tile_list[1][r].getLabel() == tile_list[0][r].getLabel():
            tile_list[1][r].doubleLabel()
            tile_list[0][r].changeLabel(0)
            moved = True
            points_added += tile_list[1][r].getLabel()
        right_and_left_check(r, tile_list)
        
        for c in range(4):
            tile_list[c][r].changeText(win)
            tile_list[c][r].updateFill()

    return points_added, moved

def move_left(win, tile_list):
    points_added = 0
    moved = False
    for r in range(4):
        while tile_list[0][r].getEmpty() == True:
            if tile_list[1][r].getEmpty() == False:
                tile_list[0][r].changeLabel(tile_list[1][r].getLabel())
                tile_list[1][r].changeLabel(tile_list[2][r].getLabel())
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            elif tile_list[2][r].getEmpty() == False:
                tile_list[1][r].changeLabel(tile_list[2][r].getLabel())
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            elif tile_list[3][r].getEmpty() == False:
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            else:
                break
            right_and_left_check(r, tile_list)
        while tile_list[1][r].getEmpty() == True:
            if tile_list[2][r].getEmpty() == False:
                tile_list[1][r].changeLabel(tile_list[2][r].getLabel())
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            elif tile_list[3][r].getEmpty() == False:
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            else:
                break
            right_and_left_check(r, tile_list)
        while tile_list[2][r].getEmpty() == True:
            if tile_list[3][r].getEmpty() == False:
                tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
                tile_list[3][r].changeLabel(0)
                moved = True
            else:
                break
            rigth_and_left_check(r, tile_list)
        if tile_list[0][r].getLabel() == tile_list[1][r].getLabel():
            tile_list[0][r].doubleLabel()
            tile_list[1][r].changeLabel(tile_list[2][r].getLabel())
            tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
            tile_list[3][r].changeLabel(0)
            moved = True
            points_added += tile_list[0][r].getLabel()
        if tile_list[1][r].getLabel() == tile_list[2][r].getLabel():
            tile_list[1][r].doubleLabel()
            tile_list[2][r].changeLabel(tile_list[3][r].getLabel())
            tile_list[3][r].changeLabel(0)
            moved = True
            points_added += tile_list[1][r].getLabel()
        if tile_list[2][r].getLabel() == tile_list[3][r].getLabel():
            tile_list[2][r].doubleLabel()
            tile_list[3][r].changeLabel(0)
            moved = True
            points_added += tile_list[2][r].getLabel()
        rigth_and_left_check(r, tile_list)
        for c in range(4):
            tile_list[c][r].changeText(win)
            tile_list[c][r].updateFill()
    return points_added, moved

def up_and_down_check(c, tile_list):
    for tile in tile_list[c]:
        if tile.getLabel() == 0:
            tile.emptySquare()
        else:
            tile.fillSquare()

def right_and_left_check(r, tile_list):
    for c in range(4):
        if tile_list[c][r].getLabel() == 0:
            tile_list[c][r].emptySquare()
        else:
            tile_list[c][r].fillSquare()

main()
