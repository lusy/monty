# Geometrische Objekte und Operationen

## Idee

Wir wollen unser Wissen über Klassen in Python anwenden um Geometrische
Objekte abzubilden und zu zeichnen. In der Datei **geometry.py** befindet sich
ein Grundgerüst mit dem ihr arbeiten könnt.

## Implementierung

Wir wollen mindestens drei Klassen erstellen:

* Geometry - Die Basisklassen von der alle anderen geometrischen Objekte erben
* Point - Eine Klasse, die einen Punkt in der Ebene darstellt
* LineSegment - Eine Klasse, die eine Strecke in der Ebene darstellt

Die Point- und LineSegment-Klasse soll von Geometry das *fill* Attribute
erben, das wir zum Rendern der Punkte und Linien benutzen.

Die Point-Klasse soll wie folgt instanziert werden können:

    Point(0, 0)
    Point(0, 0, "purple")

Die Line-Klasse soll wie folgt instanziert werden können:

    Line(Point(0, 0), Point(1, 1))
    Line(Point(0, 0), Point(1, 1), "red")


## Erweiterungen

1. Verändere die Größe des Fensters
    1. Bonuspunkte, wenn man dem Programm die Größe als Paramater übergeben kann
2. Wir möchten Linien gerne standarmäßig pink rendern und Punkte blau
3. Füge andere geometrische Objekte hinzu, z.B. Linienzüge, Rechtecke

## Implementierung (Bonus)

Implementiere eine *intersetcs* Funktion, die überprüft, ob sich die
geometrischen Objekte schneiden. Nutze die unter anderem die `isinstance`
Funktion umzu überprüfen mit welchem geometrischen Objekt du arbeitest.
