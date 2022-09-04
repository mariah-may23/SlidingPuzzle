'''

Mariah Maynard
CS5001 Final Project
Sliding Puzzle Game

'''
import turtle
import random
import time

screen = turtle.Screen()

class Tiles:
    """
        Makes each tile in the game a turtle object
        Performs different actions
    """
    def __init__(self, image, size, name, square, num) -> None:
        self.turtle = turtle.Turtle(visible=False)
        self.turtle.penup()
        self.turtle.image = image
        self.turtle.name = name
        self.size = size
        self.square = square
        self.num = num
        screen.addshape(image)
        self.turtle.shape(image) # each turtle will take the image of a tile

    def seen(self):
        """Tile shows itself"""
        return self.turtle.showturtle()

    def position(self):
        """Retrieve tile's position in x,y coordinates"""
        return self.turtle.position()

    def xcoord(self):
        """Retrieve the tile's x coordinated"""
        return self.turtle.xcor()

    def ycoord(self):
        """Retrieve tile's y coordinate"""
        return self.turtle.ycor()

    def go_here(self, x, y):
        """Sends tile to a specific position"""
        return self.turtle.goto(x,y)

    def swap(self, other):
        """Swaps tile's position with another tile's position"""
        s = self.position()
        o = other.position()
        self.turtle.goto(o)
        other.turtle.goto(s)


    def place_tile(self) -> list:
        """"
            Purpose: Places the tiles into their positions
            Parameter: None
            Returns: A list of the correct tile positions
        """
        tile_pos = []  # creating list of tile positions

        for row in range(4, 0, -1):
            for column in range(1, 5, 1):
                tile_pos.append([column * 110 - 380, row * 110 - 180])

        pos = int(self.num - 1)  # take position of tile from list

        if self.square == 4:
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(tile_pos[pos][0], tile_pos[pos][1])
        # self.turtle.showturtle()

            return tile_pos
        if self.square == 3:
            mod_pos = tile_pos[:3]+tile_pos[4:7]+tile_pos[8:11]
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(mod_pos[pos][0], mod_pos[pos][1])

            return mod_pos
        if self.square == 2:
            mod_pos = tile_pos[:2] + tile_pos[4:6]
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(mod_pos[pos][0], mod_pos[pos][1])
            return mod_pos


    def shuffle_tile(self, shuffled_tile_pos: list) -> list:
        """"
            Purpose: Places the tiles into their shuffled positions
            Parameter: List of true positions, self
            Returns: A list of the shuffled tile positions
        """

        pos = int(self.num - 1)  # take position of tile from list


        self.turtle.penup()
        self.turtle.speed('fastest')
        self.turtle.goto(shuffled_tile_pos[pos][0], shuffled_tile_pos[pos][1])
        self.turtle.showturtle()

        return shuffled_tile_pos

    def reset(self) -> list:
        """"
            Purpose: Places the tiles into their true positions
            Parameter: Self
            Returns: None
        """
        tile_pos = []  # creating list of tile positions

        for row in range(4, 0, -1):
            for column in range(1, 5, 1):
                tile_pos.append([column * 110 - 380, row * 110 - 180])

        pos = int(self.num - 1)  # take position of tile from list

        if self.square == 4:
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(tile_pos[pos][0], tile_pos[pos][1])
        # self.turtle.showturtle()

            #return tile_pos
        if self.square == 3:
            mod_pos = tile_pos[:3]+tile_pos[4:7]+tile_pos[8:11]
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(mod_pos[pos][0], mod_pos[pos][1])

            #return mod_pos
        if self.square == 2:
            mod_pos = tile_pos[:2] + tile_pos[4:6]
            self.turtle.penup()
            self.turtle.speed('fastest')
            self.turtle.goto(mod_pos[pos][0], mod_pos[pos][1])
            #return mod_pos
        self.turtle.showturtle()



class Buttons:
    """Places buttons for user options"""
    def __init__(self, image):
        self.turtle = turtle.Turtle(visible=False)
        self.image = image
        self.turtle.image = image
        screen.addshape(image)
        self.turtle.shape(image)
        self.turtle.speed('fastest')

    def position(self):
        """Retrieves button's position"""
        return self.turtle.position()

    def xcoord(self):
        """Retrieves button's x coordinate"""
        return self.turtle.xcor()

    def ycoord(self):
        """Retrieves button's y coordinate"""
        return self.turtle.ycor()

    def seen(self):
        """Shows button"""
        return self.turtle.showturtle()

    def place(self, x, y):
        """Places button at specific location"""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.seen()

    def button_click(self, on_clicks):
        """Checks if button is clicked on"""
        return self.turtle.onclick(on_clicks)




