#-*- coding: utf-8 -*-
from Tkinter import *

class Geometry(object):

    def __init__(self, ...):
        self.fill = ...

    def draw(canvas):
        raise Exception("Overwrite in super class")

    def intersects(geom):
        raise Exception("Not implemented")

class LineSegment(...):

    ...

    def draw(self, canvas):
        # Zeichne eine Linie
        canvas.create_line(self.src.x, self.src.y, self.dst.x, self.dst.y, fill=self.fill)

class Point(...):

    def __init__(...):
        super(..., self).__init__(...)
        ...

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
    line = ...
    line2 = ...
    point = ...

    # Geometrische Objekte zeichnen
    point.draw(canvas)
    line.draw(canvas)
    line2... # zweite line zeichnen

    mainloop()
