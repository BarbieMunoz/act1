"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

#import turtle to use the circle method
import turtle
from turtle import * 

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    #Get radius using the eucladian distance between start and end
    radio = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    #use turtles circle method to draw the circle
    turtle.circle(radio)
    end_fill()



def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    contador = 0

    # contador para cambiar el tamaño de la línea y sea un rectangulo
    for count in range(4):
        if contador % 2 == 0:
            forward(end.x - start.x)
            left(90)
        else:
            forward(end.y - start.y)
            left(90)

        contador += 1
    end_fill()

    
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # lo importante de esto es cambiar el ángulo para que se cree bien
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value

#declare hexadecimal value for a new lightblue color
light_blue = "#9DF4EF"

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Use new color with a new binded keybind, passing the string as a parameter for color
onkey(lambda: color(light_blue), 'Q')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
