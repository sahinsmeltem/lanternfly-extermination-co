print('Lanternfly Extermination Co.')
print('hello')

from cmu_graphics import * 

def onAppStart(app):
    app.width = 400
    app.height = 600


def redrawAll(app):
    drawRect(100, 100, 100, 100, fill = 'red')

def main():
    runApp()
main()
