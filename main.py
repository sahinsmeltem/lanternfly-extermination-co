print('Lanternfly Extermination Co.')

from cmu_graphics import * 
import random

def onAppStart(app):
    app.flies = [ ]
    app.width = 400
    app.height = 600
    generate


def onStep(app):
    pass


def onMousePress(app, mouseX, mouseY):
    r = random.randrange(5, 50)
    color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    dot = makeDot(mouseX, mouseY, r, color)
    app.dots.append(dot)
    print('Added:', dot)
    

def redrawAll(app):


class Fly:
    def __init__(self, cx, cy, size, bTime):
        self.cx = cx
        self.cy = cy
        self.size = size
        self.color = 'black'
        return dot

    
    def draw(self):
        



def main():
    runApp()
main()

