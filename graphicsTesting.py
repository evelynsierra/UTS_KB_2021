from graphics import *


def main():
    win = GraphWin('Face', 200, 150) # Judul dan dimensi
    # win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center dan radiusnya
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # end points
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corner dari box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Klik dimana pun untuk keluar.')
    message.draw(win)
    print(win.getKey())
    win.close()
if __name__ == "__main__":
    main()
