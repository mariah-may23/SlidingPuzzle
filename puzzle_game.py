'''

Mariah Maynard
CS5001 Final Project
Sliding Puzzle Game

'''
import tkinter
import turtle
import time
import math
import random
import os

from puzzle_classes import Tiles
from puzzle_classes import Buttons
screen = turtle.Screen()


def b_options(n, tile_obj, name):
    '''
        Purpose: Allow user to reset, load, or quit a puzzle
        Parameters: List of tile object and positions, number of tiles
        Returns: None
    '''

    def reset_click(x: int, y: int) -> None:
        """ Resets puzzle pieces to their true positions"""
        positions = []
        for num in range(1, n+1):
            positions.append(tile_obj[num][0].turtle.position()) # store current positions in a list
        for num in range(1, n + 1):
            tile_obj[num][0].reset() # put all tiles in proper position
        time.sleep(2)
        for num in range(1, n + 1):
            tile_obj[num][0].turtle.goto(positions[num - 1]) # place tiles back in current position

    # placing reset button
    reset_b = Buttons('Resources/resetbutton.gif')
    reset_b.place(100, -300)
    reset_b.button_click(reset_click)

    def load_click(x: int, y: int) -> None:
        """Loads new puzzle of user's choice"""
        puz_files = []

        for file in os.listdir('./'):
            if file.endswith(".puz"):
                puz_files.append(file)

        for i, j in enumerate(puz_files):
            if 'malformed' in j:
                del puz_files[i]

        files = "\n".join(puz_files)
        choice = screen.textinput("Load Puzzle", f"Enter the name of the puzzle you wish to load. Choices are:\n{files}")
        tiles, tile_info = read_puz(choice)
        attempts = attempts_popup()
        #name = name_popup()
        screen.clearscreen()
        format_screen()
        create_gameboard(tiles, tile_info, attempts, name)


    # placing load button
    load_b = Buttons('Resources/loadbutton.gif')
    load_b.place(200, -300)
    load_b.button_click(load_click)


    def quit_click(x: int, y: int):
        """Closes out the game"""
        quit_box = turtle.Turtle(visible=False)
        quit_box.penup()
        quit_box.shape('square')
        quit_box.shapesize(10, 20, 12)
        quit_box.fillcolor('blue')
        quit_box.goto(0,0)
        quit_box.stamp()
        quit_box.goto(-110,-20)
        quit_box.write("You have quit the game!\nThanks for playing\nBetter luck next time", font=('Arial', 20, 'bold'))
        time.sleep(3)
        screen.clearscreen()
        screen.bye()

    # placing quit button
    quit_b = Buttons('Resources/quitbutton.gif')
    quit_b.place(300, -300)
    quit_b.button_click(quit_click)




def attempts_popup() -> int:
    """"
        Purpose: Prompt for user information
        Parameter: None
        Returns: Integer representing number of attempts user has
    """

    attempts = screen.numinput("Attempts", "Enter the number of moves you want (5-200)", minval=5, maxval=200)
    attempts = int(attempts)


    return attempts

def name_popup() -> str:
    """"
        Purpose: Prompt for user information
        Parameter: None
        Returns: String representing user's name
    """

    name = screen.textinput("Player Name", "Enter your name: ")
    return name



def draw_shape(width: int, height: int, turtle) -> None:
    """"
        Purpose: Draw squares
        Parameter: Integers for width and height of square, turtle object
        Returns: None
    """

    turtle.pendown()
    turtle.pensize(5)
    for i in range(2):
        turtle.speed("fastest")
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def splash_screen() -> None:
    '''
        Purpose: Creates a splash screen at beginning of game
        Parameters: None
        Returns: None
    '''

    s1 = turtle.Turtle()
    screen.setup(800, 800)
    screen.addshape("./Resources/splash_screen.gif")
    s1.shape("./Resources/splash_screen.gif")
    time.sleep(2)
    s1.hideturtle()


def format_screen() -> None:
    '''
        Purpose: Formats the screen to include a background
        Parameters: None
        Returns: None
    '''
    screen.bgcolor('black')
    board = turtle.Turtle(visible=False)

    # creating game space for tiles
    board.pencolor('magenta')
    board.penup()
    board.goto(-350,350)
    draw_shape(500, 550, board)



    # creating player options/moves space
    board.penup()
    board.goto(-350, -250)
    board.pencolor('magenta')
    draw_shape(700, 100, board)
    board.penup()
    board.goto(-300, -310)
    board.pencolor('lemon chiffon')
    board.write("Player Moves:", font=('Arial', 20, 'bold'))

    #creating leaderboard space
    board.penup()
    board.goto(175, 350)
    board.pencolor('light green')
    draw_shape(175, 550, board)
    board.penup()
    board.goto(200, 320)
    board.write("Leaders:", font=('Arial', 16, 'bold'))




def create_gameboard(tiles: dict, tile_info: dict, attempts: int, player_name: str) -> None:
    """
        Purpose: Set-up the game by calling the necessary classes
        Parameters: A dictionary containing info about the tiles, A dictionary containing tile images
        Returns: None
    """
    game = turtle.Turtle(visible=False)

    # creating thumbnail stamp near leaderboard
    try:
        screen.addshape(tile_info['thumbnail'])
        game.shape(tile_info['thumbnail'])
        game.penup()
        game.goto(335, 335)
        game.stamp()
    except:
        current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        error = f"\n{current_time} ERROR: {tile_info['thumbnail']} does not exist. LOCATION: create_gameboard()"
        error_log(error)

    # create move counter
    moves = 0
    move = turtle.Turtle(visible=False)
    move.penup()
    move.pencolor('white')
    move.goto(-100, -310)
    move.write(f"{moves}", font=('Arial', 20, 'bold'))
    move.penup()

    #creating leaderboard
    try:
        with open('txtfiles/leaderboard.txt', mode='r') as infile:
            leaders = []
            for lines in infile:
                #lines = lines.split()
                lines = lines.strip()
                leaders.append(lines)
    except:
        current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        error = f"\n{current_time} ERROR: Could not open leaderboard.txt. LOCATION: create_gameboard()"
        error_log(error)


    leaders.sort() # sort leaders from least amount of moves to most amount of moves
    top_scorers = leaders[0:3] # only looking at the top three leaders
    top_leaders = "\n".join(top_scorers)


    game.penup()
    game.goto(200,240)
    game.pencolor('lemon chiffon')
    game.write(f"\n{top_leaders}", font=('Arial', 15, 'bold'))


    # extracting info from tile_info dictionary
    size = int(tile_info['size'])
    size = size + (110-size)
    number = int(tile_info['number']) # getting the number of tiles
    name = tile_info['name']

    number_of_tiles = int(len(tiles))
    square = math.sqrt(number_of_tiles)


    # creating new dictionary to store each tile as a turtle object
    tile_obj = {}
    n = number
    if square % 1 == 0:  # checking to see if number of tiles is a perfect square
        for num in range(1, n + 1):
            tile_obj[num] = Tiles(tiles[f'{num}'], size, name, square, num) # creating multiple turtles at once
            tile_positions = tile_obj[num].place_tile()  # true position list


        # shuffling the puzzle
        shuffled_tile_pos = tile_positions[:]  # shuffled position list
        random.shuffle(shuffled_tile_pos)


        # placing tiles in shuffled positions
        for num in range(1, n + 1):
            tile_obj[num].shuffle_tile(shuffled_tile_pos)


    for num in range(1, n + 1):
        tile_obj[num] = [tile_obj[num], [tile_obj[num].xcoord(), tile_obj[num].ycoord()]] # adding tile coord to key values

    # placing buttons
    b_options(n, tile_obj, name)



    def on_clicks(x: int, y: int) -> None:
        '''
            Purpose: Use clicked position to move tile
            Parameters: x and y values of clicked position
            Returns: None
        '''
        nonlocal moves
        d_edge = (size + (110-size)) / 2  # distance from center of tile to edge

        # storing blank tile coordinates as variables to refer back to
        blank_num = n # blank tile number will always be last
        blank_x = tile_obj[n][1][0]
        blank_y = tile_obj[n][1][1]


        for key, value in tile_obj.items(): # looking through dictionary
            if (value[1][0] - d_edge < x < value[1][0] + d_edge) and \
                    (value[1][1] + d_edge > y > value[1][1] - d_edge): # see if click is on tile
                clicked_tile_num = key
                x = value[1][0] # store tile x
                y = value[1][1] # store tile y

                # check all directions of clicked tile, if blank is NSEW then swap with blank
                if  (blank_x == x + size and blank_y == y) or \
                        (blank_x == x - size and blank_y == y) or \
                        (blank_x == x and blank_y == y + size) or \
                        (blank_x == x and blank_y == y - size):

                    tile_obj[clicked_tile_num][0].swap(tile_obj[blank_num][0])

                    # update the dictionary so the tile positions reflect new positions
                    tile_obj[clicked_tile_num][1], tile_obj[blank_num][1] = tile_obj[blank_num][1], tile_obj[clicked_tile_num][1]
                    player_tiles = []
                    for num in range(1, n+1):
                        player_tiles.append([tile_obj[num][0].xcoord(), tile_obj[num][0].ycoord()])

                    # check to see if current tile positions match the correct positions
                    if player_tiles == tile_positions: # they win
                        print("yay, you won")
                        move.penup()
                        move.shape('square')
                        move.shapesize(2, 10, 5)
                        move.fillcolor('yellow')
                        move.goto(-30, 0)
                        move.stamp()
                        move.goto(-110, -18)
                        move.write("\n   Yay! You won!", font=('Arial', 20, 'bold'))
                        close_game(player_name, moves)

                    if (tile_obj[clicked_tile_num][1][0] , tile_obj[clicked_tile_num][1][1]) != (tile_obj[blank_num][1][0], tile_obj[blank_num][1][1]):

                        # update move counter
                        if attempts > moves:
                            moves += 1
                            move.clear()
                            move.write(f"{moves}", font=('Arial', 20, 'bold'))
                            move.penup()
                        if attempts == moves:
                            move.penup()
                            move.shape('square')
                            move.shapesize(5, 15, 5)
                            move.fillcolor('yellow')
                            move.goto(-30, 0)
                            move.stamp()
                            move.goto(-110, -20)
                            move.pencolor('black')
                            move.write("\n         You lose!\nBetter luck next time!", font=('Arial', 15, 'bold'))
                            close_game(player_name, moves)

    # get user clicks
    screen.onclick(on_clicks)


def close_game(player_name: str, moves: int) -> None:
    """
        Purpose: End the game
        Parameter: Player's name and number of moves they used
        Returns: None
    """

    with open('txtfiles/leaderboard.txt', mode='a') as infile:
        infile.write(f"{moves}: {player_name}\n")
        infile.close()
    time.sleep(3)
    screen.bye()


def read_puz(puz_filename: str) -> tuple:
    """
        Purpose: Store information contained in puz file
        Parameter: File specific to puz file
        Returns: Dictionary of puz file info, Dictionary of puz file images
    """

    try:
        with open(puz_filename, mode='r') as infile:
            tile_info = {}  # creating dictionary with the tile name, number, size and thumbnail
            for lines in infile:
                lines = lines.split()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace(":", "")
                tile_info[lines[0]] = lines[1]
                if 'thumbnail' in lines:
                    tiles = {} # begins new dictionary with tile images only
                    for lines in infile: 
                        lines = lines.split()
                        for i in range(len(lines)):
                            lines[i] = lines[i].replace(":", "")
                        tiles[lines[0]] = lines[1]

    except:
        current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        error = f"\n{current_time} ERROR: {puz_filename} does not exist. LOCATION: read_puz()"
        error_log(error)

    return tiles, tile_info

def error_log(error) -> None:
    '''
        Purpose: Updates the error log for future improvements
        Parameters: Current error
        Returns: None
    '''

    with open('txtfiles/5001_puzzle.err.txt', mode='a') as infile:
        infile.write(f"{error}")
        infile.close()


def main():
    splash_screen()
    player_name = name_popup()
    attempts = attempts_popup()
    format_screen()
    puzzle = 'mario.puz'
    tiles, tile_info = read_puz(puzzle)
    create_gameboard(tiles, tile_info, attempts, player_name)
    turtle.done()

if __name__ == "__main__":
    main()