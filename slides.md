# Konzept:

## Tag 0:

Einführung in Python mit DIY-Einschüben
Schließt ab mit einem Mini-Projekt

##Tag 1:

Größeres Projekt aka Riesen-Projekt

##Tag 2:

siehe oben

Mögliche Projekte:

* Punkt/Linie/Bla/Geometriekramm
* sinnloses Textadventure
* Lexer/Compiler
* grep

# python

Was ist Python?

# Python installieren

    aptitude install python3
    
Für Windows:

>Get your self a fucking os.

# Good to know

* Interpretierte Sprache
* dynamisch getypt

# Erste Schritte

    $ python
    Python 2.7.3 (default, Aug  1 2012, 05:16:07) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

# Erste Schritte 02 
(Skripte schreiben^^)

* Editor öffnen
* Datei foo.py anlegen
* print("Hello World") schreiben
* python foo.py ausführen

# Dokumentation

Wo finde ich Dokumentation?

* pydoc
* official documentation http://docs.python.org/3/
* tutorial: http://docs.python.org/3/tutorial/index.html
* lib ref: http://docs.python.org/3/library/index.html
* language ref: http://docs.python.org/3/reference/index.html

# Objekte

In python is alles ein Objekt. Es gibt verschiedene Typen von Objekten:

* Numbers: integer, reals
* boolean
* strings
* listen
* dictionaries
* tupel

# Variablen

    x = 1
    pi = 3.145
    y = pi

# Variablen reassignment

    pi = 2.4
    x = 2
    # jetzt zeigen sowohl pi=2.4 als auch y = 2.4; x ist 2
    
    
### Aufgabe


# Datentypen

## Numbers

    1
    3.145
    
## Operatoren auf Zahlen

    1 + 1
    2 - 1
    2 * 3
    10 / 0.0
    4 / 5
    5 % 2
    1 ** 2
    
### Aufgabe:

Was passiert wenn wir `5 + 3 / 2.0` eingeben?

Was passiert hier: `4 / 2 / 2`

Sinnvolle Aufgaben hier einfügen!

## Boolean

    True
    False

## Boolean operators

    not False
    True and True
    False or True

### Aufgabe

Zu was wird der folgenden Ausdruck ausgewertet:

    False or True and False
    True and (True or False)
    False or True and not False
    
## Strings

    "foo"
    'bar lalala'
    """
    blabla
    blup
    blip
    """

## String operators

    "Hello " + "World"
    "Hello"[0]
    "Hello"[-1]
    "Hello"[1:4]
    "hello".upper()
    "hello".lower()

### Aufgabe

Erstelle eine String mit deinem Namen und lass ihn in Großbuchstaben erscheinen.
Lass dir von dem String nur den Substring ausgeben, der deinen Vornamen enthält.

Finde andere Funktionen, die man auf Strings anwenden kann. Was Funktionen sind erklären wir später.

## Listen
    
Listen können erweitert oder verkleinert werden.
Man kann auf einzelne Listenelemente zugreifen und die manipulieren
    
    []
    [0,1,3,4,5]
    ["Egon", "Bert", "Hildegard", "Dörte"]
    ["Egon", 2.4, "Bert", True] # es müssen nicht alle Werte vom selben Datentyp sein
    [9,8,7,6,5,4,3,2,1][4]
    
    a = [0,1,2,3,4,5]
    a.append(6)
    
### Aufgabe
    
    l = ["Egon", "Bert", "Hildegard", "Dörte"]
    
Füge noch Ingo und Isolde zur Liste l hinzu. 
Gibt es da eine weitere Möglichkeit außer die einzeln mit `append()` hinzuzufügen?
Füge Friedrich Wilhelm Maximilian (Achtung!: Das ist ein Name und nicht drei!)
an 3. Stelle in die Liste ein.
An welcher Stelle befindet sich Hildegard?
Wer ist an 4. Stelle?
Lösche Bert aus der Liste.

Speichere die Antworten auf die Fragen in einzelne Variablen.

Um die Fragen zu beantworten kannst du in die Dokumentation nach geeigneten Funktionen schauen.
    

    
## Dictionaries (Wörterbücher)

    {}
    {"Lusy":"toll", "Philipp": "lol"}
    
### Aufgabe

    d = {'Egon':123456}

Erweitere das Dictionary d, so dass es die Telefonnumern von 3 weiteren Menschen 
enthält (also, du kannst die Namen als Keys verwenden). 
Füge 2 weitere Nummern hinzu.
Speichere die Nummer von Egon in der variable egon, indem du sie im Dictionary
nachschaust.

## Tupel 
    # tupel sind unveränderbar (immutable)
    ("lala",'blup',"rrt")
    
    b = ("lala",'blup',"rrt")
    b.append("la") # geht nicht 
    
### Aufgabe

Erstelle 3 Zweiertupel (und speichere die jeweils in Variablen), die als Elemente
3 der Name-Telefonnummer-Paare aus der Dictionaries-Aufgabe haben.

    
# Funktionen

* generalized Beheavior vs. specialized Behaviour
* reusable
* können Ergebnis zurückliefern

    def say_hello(): # Kopf
        return "Hello" # Rumpf
        
# Objekte und Funktionen

    "Egon".upper()
    bar = [1,2,3,4]
    bar.reverse()

# Beispiele für vordefinierte Funktionen

    len()
    str()
    print()

# Kontrollfluß
    nützlich wenn man längere Programme in einer Datei definiert

## if

    if god_is_happy:
        sun = "is shining"
        
## if-else

    if god_is_happy:
        sun = "is shining"
    else:
        sun = "isn't shining"

## if-elif-else

      if god == "is_happy":
        sun = "is shining"
      elif god == "is_sad":
        sun = "isn't shining"
      else:
        sun = "invalid option"
    
## While-Schleife

    while(True):
        print("endless")

## For-Schleife

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    
## Break/Continue

    insert example here
    
## Try/Except

Wann braucht man die überhaupt?
    
    def bad_function():
        raise Exception("Booommm")
    
    try:
        bad_function() 
    except Exception, e:
        print("catched: " +  e)

# Module

Module sind logische Einheiten, die man benutzt, um Code zu organisieren.

    import sys
    iport time
    from sys import stdout

# Eingabe / Ausgabe

## sdtin/sdtout/stderr

    name = raw_input("Tell me your name")
    print(name)
    print("So, your name is %s" % name)
    

## for real

    import sys
    sys.stdout.write("fooo\n")
    sys.stderr.write("This is an error message\n")
    
    sys.stdin.read()

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

### Aufgabe

1. Eine Datei einlesen, z.B. den Code eures Programms
2. Inhalt der Datei in eine andere Datei schreiben
3. also known as `cp`
4. 

### Aufgabe2

1. Schreibe in eine Datei deinen Namen, dein Geburtsdatum, deine Schuhgröße, 
deine Lieblingsfarbe, ob du Katzen magst und die ersten 2 Zeilen von deinem 
Lieblingslied. Alle Angaben sollen auf eine neue Zeile kommen nach dem Muster

    Schuhgröße: 42
    Ich mag schwarze Katzen.
    ...

2. Mach die Datei zu.
3. Öffne die Datei erneut, diesmal in Lesemodus.
4. Lese die Datei Zeile für Zeile aus (Doku angucken ;))



# Main-Funktion

    __main__
    
# Klassen Definition

    class Dog(object):
        legs = 4
        barks = True
        
        def __init__(self, name, owner):
            self.name = name
            self.owner = owner


# Objekte instanzieren


    sharo = Dog("sharo", "philipp")
    egon = Dog("egon", "lusy")


# Vererbung

Hier ein sinnfreies Beispiel:

    class Animal(object):
        hearts = 1
        legs = 0
        favorite_food = ""
    
    class Dog(Animal):
        legs = 4
        favorite_food = "köfte"
        
    class Human(Animal):
        legs = 2
        favorite_food = "falafel"
        drinks_beer = True
        hobbys = ["plays the piano", "plays chess"]
        
    class Nerd(Human):
        favorite_food = "pizza"
        likes_computers = True
        hobbys = ["painting", "ponnies"]
    
# Klassen?
    * objekte instanziieren
    * main()
    * self


# Anonyme Funktionen 
    //vlt zu hardcore?

    lambda x: x**2

# [List comprehensions](http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)

    squares = [x**2 for x in range(10)]



# Funktionale Programmierung in Python

    map(lambda x: x**2, range(10))
    filter(lambda x: x % 2 == 0, range(10))


# Python-Tools

## pip (python package index)

> A tool for installing and managing Python packages

Website: [http://www.pip-installer.org/en/latest/](http://www.pip-installer.org/en/latest/)

## virtualenv

> Virtual Python Environment builder

Website: [https://pypi.python.org/pypi/virtualenv](https://pypi.python.org/pypi/virtualenv)

## ipython

> a rich architecture for interactive computing

Website: [http://ipython.org](http://ipython.org)

# Peps

Python Enhancement Proposals

Website: [http://www.python.org/dev/peps/](http://www.python.org/dev/peps/)




