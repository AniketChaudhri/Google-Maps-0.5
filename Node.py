"""
Foundation for implementation of project.
Works as the grid analogue of graph data structure

Code written by Rajat Singh
"""


from math import inf
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 111, 255)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 255)
YELLOW = (255, 255, 0)
GREY = (143, 143, 143)
BROWN = (186, 127, 50)
DARK_GREEN = (0, 128, 0)
DARKER_GREEN = (0, 50, 0)
DARK_BLUE = (0, 0, 128)
MAROON = (128, 0, 0)
DARK_ORANGE = (235, 143, 52)
MAGENTA = (235, 52, 229)
PINK = (255, 192, 203)


# Make it easier to add different node types
class Node():

    nodetypes = ['blank', 'start', 'end', 'wall',
                 'mud', 'trafficlow', 'traffichigh', 'dormant']

    colors = {'regular': {'blank': WHITE, 'start': MAGENTA, 'end': LIGHT_BLUE, 'wall': BLACK, 'mud': BROWN, 'trafficlow': ORANGE, 'traffichigh': RED,  'dormant': GREY},
              'visited': {'blank': GREEN, 'start': MAGENTA, 'end': LIGHT_BLUE, 'wall': BLACK, 'mud': DARK_GREEN, 'trafficlow': ORANGE, 'traffichigh': RED, 'dormant': GREY},
              'path': {'blank': BLUE, 'start': MAGENTA, 'end': LIGHT_BLUE, 'wall': BLACK, 'mud': DARK_BLUE, 'trafficlow': DARK_BLUE, 'traffichigh': PURPLE, 'dormant': GREY}
              }

    distance_modifiers = {'blank': 1, 'start': 1, 'end': 1, 'wall': inf,
                          'mud': 3, 'trafficlow': 2, 'traffichigh': 4, 'dormant': inf}

    def __init__(self, nodetype, text='', colors=colors, dmf=distance_modifiers):
        self.nodetype = nodetype
        self.rcolor = colors['regular'][self.nodetype]
        self.vcolor = colors['visited'][self.nodetype]
        self.pcolor = colors['path'][self.nodetype]
        self.is_visited = True if nodetype == 'start' else True if nodetype == 'end' else False
        self.is_path = True if nodetype == 'start' else True if nodetype == 'end' else False
        self.distance_modifier = dmf[self.nodetype]
        self.color = self.pcolor if self.is_path else self.vcolor if self.is_visited else self.rcolor

    def update(self, nodetype=False, is_visited='unchanged', is_path='unchanged', colors=colors, dmf=distance_modifiers, nodetypes=nodetypes):
        if nodetype:
            assert nodetype in nodetypes, f"nodetype must be one of: {nodetypes}"
            if (self.nodetype == ('start' or 'end')) and (nodetype == ('wall' or 'mud' or 'trafficlow' or 'traffichigh')):
                pass
            else:
                self.nodetype = nodetype

        if is_visited != 'unchanged':
            assert type(
                is_visited) == bool, "'is_visited' must be boolean: True or False"
            self.is_visited = is_visited

        if is_path != 'unchanged':
            assert type(
                is_path) == bool, "'is_path' must be boolean: True or False"
            self.is_path = is_path

        self.rcolor = colors['regular'][self.nodetype]
        self.vcolor = colors['visited'][self.nodetype]
        self.pcolor = colors['path'][self.nodetype]
        self.distance_modifier = dmf[self.nodetype]
        self.color = self.pcolor if self.is_path else self.vcolor if self.is_visited else self.rcolor
