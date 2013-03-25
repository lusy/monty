---
title       : Python class
subtitle    : for beginners
author      : Lyudmila Vaseva (vaseva@mi.fu-berlin.de)
job         : Philipp Borgers (borgers@mi.fu-berlin.de)
framework   : io2012        # {io2012, html5slides, shower, dzslides, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      #
widgets     : []            # {mathjax, quiz, bootstrap}
mode        : selfcontained # {standalone, draft}
---

## Konzept:

### Tag 0:

Einführung in Python mit DIY-Einschüben

Schließt ab mit einem Mini-Projekt

### Tag 1:

Größeres Projekt aka Riesen-Projekt

Mögliche Projekte:

* Punkt/Linie/Bla/Geometriekramm
* sinnloses Textadventure
* Lexer/Compiler
* grep

---

## python

### Was ist Python?

* Interpretierte Sprache
* dynamisch getypt
* klare Syntax, flache Lernkurve
* verschiedenen Programmierparadigmen:
    * imperativ
    * funktional
    * objekt-orientiert

---

![XKCD](http://imgs.xkcd.com/comics/python.png)

Attribution: http://xkcd.com

---

## Python installieren

    $ # debian/ubuntu
    $ aptitude install python3
    $ # arch
    $ pacman -S python3

Für Windows:

> Get yourself a fucking os.

Sollte das unmöglich sein:
[http://www.python.org/getit/](http://www.python.org/getit/)

---

## Erste Schritte
### Python Interpreter

    $ python3
    Python 3.2.3 (default, Oct 19 2012, 20:13:42)
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Mit `Strg + D` oder `exit()` wird die Python-Shell wieder beendet.

Gibt es auch in bunt:

    $ ipython3

---

## Erste Schritte 02
### (Skripte schreiben)

* Editor öffnen
* Datei foo.py anlegen
* Inhalt der Datei:

```
    print("Hello World")
```

* Durch python ausführen

```shell
    $ python foo.py
```

---

## Dokumentation

Wo finde ich Dokumentation?

* pydoc
* official documentation http://docs.python.org/3/
* tutorial: http://docs.python.org/3/tutorial/index.html
* lib ref: http://docs.python.org/3/library/index.html
* language ref: http://docs.python.org/3/reference/index.html

---

## pydoc

Im terminal:

```
    pydoc datetime
```

Als Webserver starten:

```
    pydoc -p 1337
```

---

## Objekte

In python is alles ein Objekt. Es gibt verschiedene Typen von Objekten:

* Numbers: integer, reals
* boolean
* strings
* listen
* dictionaries
* tupel

---

## Variablen

    x = 1
    pi = 3.145
    y = pi

---

## Datentypen

---

## Zahlen

    1
    3.145

---

## Operatoren auf Zahlen

```python
    1 + 1
    2 - 1
    2 * 3
    10 / 0.0
    4 / 5
    5 % 2
    1 ** 2
```

---

## Aufgabe:

Was passiert wenn wir `5 + 3 / 2.0` eingeben?

Was passiert hier: `4 / 2 / 2` ?

Und hier `7 / 2` ?
Was sollte man tun, um die Antwort `3.5` zu bekommen?

Sinnvolle Aufgaben hier einfügen!

---

## Boolean

```python
    True
    False
```

---

## Boolean operators

```python
    not False
    True and True
    False or True
```

---

## Aufgabe

Zu was wird der folgenden Ausdruck ausgewertet:

```python
    False or True and False
    True and (True or False)
    False or True and not False
```

---

## Strings

    "foo"
    'bar lalala'
    """
    blabla
    blup
    blip
    """
    "And I'm saying \"Hello!\""
    "There you go!\n"

---

## String operators

    "Hello " + "World"
    "Hello"[0]
    "Hello"[-1]
    "Hello"[1:4]
    "hello".upper()
    "hello".lower()

---

## Aufgabe

Erstelle eine String mit deinem Namen und lass ihn in Großbuchstaben erscheinen.

Lass dir von dem String nur den Substring ausgeben, der deinen Vornamen enthält.

Finde andere Funktionen, die man auf Strings anwenden kann. Was Funktionen sind erklären wir später.

---

## Listen

Listen können erweitert oder verkleinert werden.

Man kann auf einzelne Listenelemente zugreifen und die manipulieren

```python
    []
    [0,1,3,4,5]
    ["Egon", "Bert", "Hildegard", "Dörte"]
    ["Egon", 2.4, "Bert", True] # es müssen nicht alle Werte vom selben Datentyp sein
    [9,8,7,6,5,4,3,2,1][4]

    a = [0,1,2,3,4,5]
    a.append(6)
```

---

## Aufgabe

```python
    names = ["Egon", "Bert", "Hildegard", "Dörte"]
```

Füge noch Ingo und Isolde zur Liste `names` hinzu.
Gibt es da eine weitere Möglichkeit außer die einzeln mit `append()` hinzuzufügen?
Füge Friedrich Wilhelm Maximilian (Achtung!: Das ist ein Name und nicht drei!)
an 3. Stelle in die Liste ein.
An welcher Stelle befindet sich Hildegard?
Wer ist an 4. Stelle?
Lösche Bert aus der Liste.

Speichere die Antworten auf die Fragen in einzelne Variablen.

Um die Fragen zu beantworten kannst du in die Dokumentation nach geeigneten Funktionen schauen.

---

## Mutable vs Immutable

* primitive datatypes are immutable: int, bool, str, long,..
Once created, contents cannot be updated.
* lists and dictionaries (following) are mutable!

---

## Mutable vs Immutable 2

Vergleich:

    names = ["Egon", "Bert", "Hildegard", "Dörte"]
    names2 = names
    names.append("Ingo")
    # names = ["Egon", "Bert", "Hildegard", "Dörte", "Ingo"]
    # names2 = ["Egon", "Bert", "Hildegard", "Dörte", "Ingo"]
    # names and names2 are two "labels" for the same list

vs

    names = names + ["Isolde"]
    # names = ["Egon", "Bert", "Hildegard", "Dörte", "Ingo", "Isolde"]
    # names2 = ["Egon", "Bert", "Hildegard", "Dörte", "Ingo"]
    # bei names wurde eine neue Liste erstellt und an wieder in die selbe Variable gespeichert

---

## Aufgabe

Füge Egon in die Liste aus der vorherigen Aufgabe ein zweites Mal hinzu.
Ist das möglich? Wie oft kommt jetzt Egon in dieser Liste vor?

Stell dir vor, wir hätten gerne eine Liste, wo alle Personen höchstens einmal vorkommen.
Was wäre eine geeignete Datenstruktur hierfür? Schau in der Dokumentation nach!

---

## Dictionaries (Wörterbücher)

    {}
    d = { "Lusy": "toll", "Philipp": "lol" }
    # Wie greife ich auf die Werte zu
    d["Lusy"]
    # Neuer Eintrag
    d["Marian"] = "blablabla"
    # man kann auch Werte im Dictionary updaten
    d["Lusy"] = "blup"

    d.keys()
    d.values()

    "Lusy" in d
    del d["Lusy"]
    "Lusy" in d

---

## Aufgabe

```python
    telefonbuch = { 'Egon': 123456, 'Paula': 030 }
```

Erweitere das Dictionary `telefonbuch`, so dass es die Telefonnummern von 3 weiteren Menschen
enthält (also, du kannst die Namen als Keys verwenden).
Schaue die Nummer von Egon in `telefonbuch` nach und speichere sie in der Variable `egon`.

---

## Tupel
    ("lala",'blup',"rrt")

    # tupel sind unveränderbar (immutable)
    b = ("lala",'blup',"rrt")
    b.append("la") # geht nicht

    # einzelne Werte zugreifen
    b[0]

    # man braucht die Klammern nicht unbedingt
    c = "Egon", "Berndt", "Dörte"

---

## Aufgabe

Speichere die Telefonnummer-Information aus der vorangegangenen Aufgabe in Tupeln.

Erstelle 3 Zweiertupel und speichere diese jeweils in Variablen, die als Elemente
drei der Name-Telefonnummer-Paare aus der Dictionaries-Aufgabe haben.

---

## Casting

Es ist möglich Typen zu konvertieren:

    int(3.145)
    float(23)
    list((1, 2))
    tuple([1,2,3])

---

## Funktionen

* generalized Behaviour vs. specialized Behaviour
* reusable
* können Ergebnis zurückliefern
* die Einrückung ist wichtig!

```python
    def say_hello(): # Kopf
        return "Hello" # Rumpf
```

---

## Funktionen mit Parametern

    def my_function(a, b):
        print(a, b)

---

## Funktionen mit Default-Parametern

    def my_function(a = 1, b = 2):
        print(a, b)

    my_function()
    my_function(2)
    my_function(3, 4)
    my_function(b = 4)

---

## Funktionen mit return-Value

    def my_function():
        return "Die Antwort auf alle Fragen"

    # vs

    def nothing():
        1 + 1

---

## Aufgabe

Definiere eine Funktion, die als Parameter deinen Namen kriegt und diesen dann printet.

Definiere eine zweite Funktion, die die Fläche eines Kreises berechnet und zurückgibt.
Welche Werte müssen hier als Parameter übergeben werden?

---

## Aufgabe2

Definiere eine Funktion, die mindesten einen Standardparameter und mindesten einen Named Argument mit einem Defaultwert.
Überlege dir einen sinnvollen Usecase, wo man so eine Funktion benutzen wollen würde.

---

## Objekte und Funktionen

```python
    "Egon".upper()
    bar = [1,2,3,4]
    bar.reverse()
    bar
```

---

## Beispiele für vordefinierte Funktionen

    sort()
    len()
    str()
    print()

---

## Kontrollfluß

---

## if

    if god_is_happy:
        sun = "is shining"

---

## if-else

    if god_is_happy:
        sun = "is shining"
    else:
        sun = "isn't shining"

---

## if-elif-else

      if god == "is_happy":
        sun = "is shining"
      elif god == "is_sad":
        sun = "isn't shining"
      else:
        sun = "invalid option"

---

## While-Schleife

    while(True):
        print("endless")

---

## For-Schleife

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

---

## Break/Continue

```python
    # break - breaks out of the smallest enclosing for or while loop
    var = 10
    while var > 0:
        print 'Current variable value :', var
        var = var -1
        if var == 5:
            break

    print "Good bye!"

    # continue - continues with the execution of the next iteration of the loop
    for letter in 'Python':
        if letter == 'h':
            continue
        print 'Current Letter :', letter
```

---

## Aufgabe

Definiere die Funktion `divisible_by_five(a)`, die einen Parameter `a` bekommt und alle Zahlen von 1 bis `a`, die durch 5 teilbar sind, ausgibt.

---

## Try/Except

Wann braucht man die überhaupt?

    def bad_function():
        raise Exception("Booommm")

    try:
        bad_function()
    except Exception, e:
        print("catched: " +  e)

---

## Module

Module sind logische Einheiten, die man benutzt, um Code zu organisieren.
Die Standard-Bibliothek enthält Module, die nützliche Funktionen zur Verfügung stellen.

    import datetime
    from datetime import datetime
    from datetime import *
    from sys import stdout as log

Jede Python-Datei ist auch ein Modul.

---

## Aufgabe zu Modulen

Nutze das datetime Modul um das aktuelle Datum zu erfragen. Berechne die
Stunden, die du seit deiner Geburt auf der Erde verbracht hast. Angenommen du
wirst 99 Jahre alt. Wie viele Sekunden bleiben dir noch?

Nutze pydoc oder die Autovervollständigung von IPython um die richtigen Klassen
und Methoden zu finden.

---

## Eingabe / Ausgabe


    name = raw_input("Tell me your name")
    print(name)
    print("So, your name is %s" % name)

---

## String Formating

```python
    name = "Egon"
    age = 142
    likes = "cat babies"
    print ("Hi! My name is %s, I'm %d years old and I like %s." % (name, age, likes))
```

---

## sdtin/sdtout/stderr

    import sys
    sys.stdout.write("fooo\n")
    sys.stderr.write("This is an error message\n")

    sys.stdin.read()

---

## Dateien einlesen und schreiben

    # LESEN
    inpFile = open("myFile", "r")
    inp = inpFile.read()
    # wenn man mit der Datei fertig ist, zumachen!
    inpFile.close()


    # Ausgabe in eine Datei schreiben
    outFile = open("myFile", "w")
    outFile.write("This is an owesome line I'm inserting in this file!\n")
    # und wieder schließen
    outFile.close()

---

## with-statement

```python
    with open("example.py") as file:
        data = file.read()
        print(data)
```

---

## Aufgabe

1. Eine Datei einlesen, z.B. den Code eures Programms
2. Inhalt der Datei in eine andere Datei schreiben
3. also known as `cp`
4.

---

## Aufgabe2

1. Schreibe in eine Datei deinen Namen, dein Geburtsdatum, deine Schuhgröße,
deine Lieblingsfarbe, ob du Katzen magst und die ersten 2 Zeilen von deinem
Lieblingslied. Alle Angaben sollen auf eine neue Zeile kommen nach dem Muster

```
    Schuhgröße: 42
    Ich mag schwarze Katzen.
    ...
```

2. Mach die Datei zu.
3. Öffne die Datei erneut, diesmal in Lesemodus.
4. Lese die Datei Zeile für Zeile aus (Doku angucken ;))


---

## Klassen Definition

```python
    class Dog(object):
        legs = 4
        barks = True

        def __init__(self, name, owner):
            self.name = name
            self.owner = owner
```

## Objekte instanzieren

```python
    sharo = Dog("sharo", "philipp")
    egon = Dog("egon", "lusy")
```

---

## Vererbung

Hier ein sinnfreies Beispiel:

    class Animal(object):
        hearts = 1
        legs = 0
        favorite_food = ""

    class Dog(Animal):
        legs = 4
        favorite_food = "köfte"

---

## Vererbung

    class Human(Animal):
        legs = 2
        favorite_food = "falafel"
        drinks_beer = True
        hobbys = ["plays the piano", "plays chess"]

    class Nerd(Human):
        favorite_food = "pizza"
        likes_computers = True
        hobbys = ["painting", "ponnies"]

---

## isinstance und type Funktion

Mit der `isinstance` kann man überprüfen, ob ein Objekt eine Instanz einer
Klasse ist:

```python
    lusy = Human()
    isinstance(lusy, Human)
```

Mit der `type` Funktion können wir den Type eines Objekts erfragen.

```python
    type(lusy)
```

---

## Main-Funktion (Programm Parameter)

    if __name__ == '__main__':

---

## Anonyme Funktionen

    lambda x: x**2

---

## [List comprehensions](http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)

    squares = [x**2 for x in range(10)]

---

## Funktionale Programmierung in Python

    map(lambda x: x**2, range(10))
    filter(lambda x: x % 2 == 0, range(10))

---

## Python-Tools

---

## pip (python package index)

> A tool for installing and managing Python packages

Website: [http://www.pip-installer.org/en/latest/](http://www.pip-installer.org/en/latest/)

---

## virtualenv

> Virtual Python Environment builder

Website: [https://pypi.python.org/pypi/virtualenv](https://pypi.python.org/pypi/virtualenv)

---

## ipython

> a rich architecture for interactive computing

Website: [http://ipython.org](http://ipython.org)

---

## Peps

Python Enhancement Proposals

Website: [http://www.python.org/dev/peps/](http://www.python.org/dev/peps/)