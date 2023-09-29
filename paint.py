"""Paint, for drawing shapes.

Exercises

1. Add a color.
    eu troquei as letras de ativação, estava maiúscula troquei por minúscula

2. Complete circle.
codigo utilizado
    raio=abs(end.x - start.x)+abs(end.y - start.y) 
    circle(raio/2)

3. Complete rectangle.
codigo utilizado
    up()
    goto(start.x, start.y)
    down()

    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)
4. Complete triangle.
codigo utilizado
    goto(end.x, start.y)
    goto(((end.x-start.x)/2)+start.x, end.y)
    goto(start.x, start.y)

5. Add width parameter.
"""

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


def circulo(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    #begin_fill()

    raio=abs(end.x - start.x)+abs(end.y - start.y) 
    circle(raio/2)
    
    #end_fill()
    pass  # TODO


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()

    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)

    pass  # TODO


def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    
    goto(end.x, start.y)
    goto(((end.x-start.x)/2)+start.x, end.y)
    goto(start.x, start.y)




    pass  # TODO


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


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'k')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'r')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
