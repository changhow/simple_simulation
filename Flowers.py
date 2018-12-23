class Flowers:
    def __init__(self, x, y, ID, color):

        if ('r' or 'R') in color:
            self.tag = rgbcolor['red']
        elif ('g' or 'G') in color:
            self.tag = rgbcolor['green']
        elif ('b' or 'B') in color:
            self.tag = rgbcolor['blue']
        elif ('y' or 'Y') in color:
            self.tag = rgbcolor['yellow']
        elif ('v' or 'V') in color:
            self.tag = rgbcolor['violet']
        elif ('ol' or 'OL') in color:
            self.tag = rgbcolor['olive']
        elif ('o' or 'O') in color:
            self.tag = rgbcolor['orange']
        elif ('i' or 'I') in color:
            self.tag = rgbcolor['indigo']
        else:
            self.tag = rgbcolor['black']

        self.id = ID
        self.color = color
        self.pos = (x, y)

"""
rgbcolor = {'violet': [120, 28, 129],
            'indigo': [64, 67, 153],
            'blue': [72, 139, 194],
            'green': [107, 178, 140],
            'olive': [159, 190, 87],
            'yellow': [210, 179, 63],
            'orange': [231, 126, 49],
            'red': [217, 33, 32],
            'black': [255, 255, 255]
            }
"""

rgbcolor = {'violet': '#8a2be2',
            'indigo': '#4B0082',
            'blue': '#0000FF',
            'green': '#00ff00',
            'olive': '#808000',
            'yellow': '#FFFF00',
            'orange': '#FFA500',
            'red': '#FF0000',
            'black': '#FFFFFF'
            }
