from MyColorMap import myColorMap as rgb_color

class Flowers:
    def __init__(self, x, y, color):

        if ('r' or 'R') in color:
            self.color = rgb_color['red']
        elif ('g' or 'G') in color:
            self.color = rgb_color['green']
        elif ('b' or 'B') in color:
            self.color = rgb_color['blue']
        elif ('y' or 'Y') in color:
            self.color = rgb_color['yellow']
        elif ('v' or 'V') in color:
            self.color = rgb_color['violet']
        elif ('ol' or 'OL') in color:
            self.color = rgb_color['olive']
        elif ('o' or 'O') in color:
            self.color = rgb_color['orange']
        elif ('i' or 'I') in color:
            self.color = rgb_color['indigo']
        else:
            self.color = rgb_color['black']

        self.tag = 'F'
        self.pos = (x, y)
