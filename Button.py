'''
Works as the GUI for buttons on Pygame interface

Code written by Adarsh Anand'''

import pygame

# For creating Buttons


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the Button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x, self.y,
                             self.width, self.height), 0)

        pygame.draw.rect(win, self.color, (self.x+1, self.y +
                         1, self.width-1, self.height-1), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 12)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + int(self.width/2 - text.get_width()/2),
                     self.y + int(self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
