# Menge (Set)

## Idee

Wir möchten gerne eine Mengen-Klasse definieren, die mit Infix-Operatoren
arbeitet. Mengen enthalten keine Duplikate.

## Implementierung

Wir implementieren die drei Operatoren:

* + (add) - Vereinigung
* - (sub) - Differenz
* or (or) - Schnittmenge

Sowie die `repr` Funktion, die eine String-Darstellung der Menge zurückliefert,
sodass wir sie `print`en können.

Die eigentlichen Daten sollen im **data** Attribute gespeichert werden. Welche
Datenstrukturen bieten sich hier für an?
