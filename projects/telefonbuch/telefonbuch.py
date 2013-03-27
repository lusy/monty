# Beispielimplementierun Telefonbuch.
# Ich habe möglichst ausführlich kommentiert, wenn was unklar ist, fragt gerne.

# Das brauchen wir für die Funktionen `save` und `load`.
import pickle
# Das speichern wir hier ein Mal, damit wir es nicht mehrmals im Code ändern
# müssen, wenn wir es ändern wollen. (Namenskonvention ist, für solche
# Konstanten Großbuchstaben zu verwenden.)
PICKLEFILE = 'telefonbuch.pickle'

# tb ist das dictionary, in dem wir die Daten speichern.
tb = {}
print('Hallo. Telefonbuch gestartet.')



while True:
    cmdstring = input('> ')
    cmd = cmdstring.split(' ')

    if cmd[0] == 'insert':
        # Hier fangen wir den Fall ab, dass jemand z.B. nur `insert` eintippt,
        # aber keinen Namen/Telefonnummer.
        try:
            name = cmd[1]
            tel = cmd[2]
        except IndexError:
            print('Zu wenige Parameter!')

        tb[name] = tel

        print('Gespeichert.')

    elif cmd[0] == 'remove':
        try:
            name = cmd[1]
        except IndexError:
            print('Zu wenige Parameter!')

        if name in tb:
            del tb[name]
            print('Gelöscht')
        else:
            print('Es gibt keinen Eintrag {}'.format(name))

    elif cmd[0] == 'get':
        name = cmd[1]

        # schöner (lies: pythoniger) als das bei remove mit `if name in tb`.
        # das mit remove ginge aber genauso
        try:
            print('Name: {} Telefonnummer: {}'.format(name, tb[name]))
        except KeyError:
            print('Es gibt keinen Eintrag {}'.format(name))

    elif cmd[0] == 'list':
        # wir iterieren über alle Einträge im Telefonbuch.
        # Bei dictionaries ist es so, dass man beim drüberiterieren
        # immer nur den Schlüssel des Eintrags bekommt. D.h. in der Variable
        # name steht dann immer der Schlüssel (was bei uns ja der Name ist)
        print('Name                 Telefonnummer       ')
        for name in tb:
            # Wir benutzen die format-Funktion, um die Daten tabellenartig
            # aufzulisten. :20 bedeutet, dass der String an dieser Stelle mit
            # Leerzeichen aufgefüllt werden soll, bis er 20 Zeichen lang ist.
            print('{:20} {:20}'.format(name, tb[name]))

    # Noch zwei Funktionen, um die Daten auch in einer Datei speichern zu
    # können. Benutzt das Pickle-Modul, das ist die beste Methode, beliebige
    # Objekte zuverlässig in Dateien zu speichern.
    # (Siehe http://docs.python.org/3/library/pickle.html)

    elif cmd[0] == 'load':
        # Das with-Konstrukt dient hier dazu, sicherzustellen, dass die Datei
        # auf jeden Fall wieder geschlossen wird, auch wenn zwischendrin ein
        # Fehler passiert.
        with open(PICKLEFILE, 'rb') as f:
            tb = pickle.load(f)
        print('Telefonbuch geladen.')

    elif cmd[0] == 'save':
        with open(PICKLEFILE, 'wb') as f:
            pickle.dump(tb, f)
        print('Telefonbuch gespeichert.')

    elif cmd[0] == 'help':
        print('Es gibt folgende Befehle:')
        print('insert name telefonnummer')
        print('remove name')
        print('get name')
        print('list')
        print('load')
        print('save')

    elif cmd[0] == 'exit':
        print('Tschüss!')
        break

    else:
        print('Unbekannter Befehl!')
