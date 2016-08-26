from graphics import *
win = GraphWin("", 100, 100)
f = open('generated.json', 'r')
array = eval(f.read())
print(array)
for (x, y, width, height, (r, g, b)) in array:
    rect = Rectangle(Point(x, y), Point(x + width, y + height))
    rect.setFill(color_rgb(r, g, b))
    # rect.setWidth(0)
    rect.draw(win)

input()
