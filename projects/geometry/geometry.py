#-*- coding: utf-8 -*-
from Tkinter import *


class Geometry(object):

    def __init__(self, fill = "black"):
        self.fill = fill

    def draw(canvas):
        raise Exception("Overwrite in super class")

class Line(Geometry):

    def __init__(self, src, dst, fill = "black"):
        super(Line, self).__init__(fill)
        self.src = src
        self.dst = dst

    def draw(self, canvas):
        # Zeichne eine Linie
        canvas.create_line(self.src.x, self.src.y, self.dst.x, self.dst.y, fill=self.fill)

class Point(Geometry):

    def __init__(self, x, y, fill = "red"):
        super(Point, self).__init__(fill)
        self.x = x
        self.y = y

    def draw(self, canvas):
        # Zeichne einen Kreis der den Punkt repräsentiert
        canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, fill=self.fill)


if __name__ == "__main__":

    # Tkinter magic
    master = Tk()

    # Verändere hier die größe des Fensters
    canvas = Canvas(master, width=800, height=800)
    canvas.pack()

    # Geometrische Objekte erzeugen
    line = Line(Point(0, 0), Point(800, 800))
    line2 = Line(Point(800, 0), Point(0, 800))
    point = Point(10, 10)

    # Geometrische Objekte zeichnen
    point.draw(canvas)
    line.draw(canvas)
    line2.draw(canvas)

    mainloop()
