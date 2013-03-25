# Telefonbuch

## Idee

Wir wollen eine kleine Anwendung schreiben, die ein Telefonbuch abbildet. Im
Telefonbuch kann man unter dem Namen einer Person eine Telefonnummer
hinterlegen. Es soll möglich sein zu einem Namen die Telefonnummer zu erfragen.
Außerdem möchten wir Einträge löschen und updaten können.

## Ideen zur Umsetzung

Die Anwendung erwartet vom Anwender Eingaben:

    * _insert_ __name__ __tefonnummer__
    * _remove_ __name__
    * _get_ __name__
    * _search_ __regex__

Nutze zur Eingabeaufforderung die `input` Funktion:

```python
    data = input(">")
```

Nutze die String-Operationen um die Eingabe zubearbeiten:

```python
    data.split(" ")
```

Nutze bedingte Anweisungen um die Eingabe des Nutzers zu überprüfen und
entsprechende Funktionen auszuführen:

```python
    if data[0] == "help":
        ...
```

Nutze Dictonaries um die Daten, die der Nutzer eingibt abzuspeichern.

## Mögliche Erweiterungen

Erweitere deine Anwendung z.B. um die Möglichkeit mehrere Telefonnummer
abzuspeichern. Du kannst auch versuchen dein Telefonbuch in ein Adressbuch
umzuwandeln.

Erweite deine Anwendung um die Möglichkeit zu einer Telefonnummer den
dazugehörigen Namen zu erhalten.
