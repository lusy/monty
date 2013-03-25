b = ("Lusy", "Marian", "Philipp")

for name in b:
    if len(name) > 4:
        print (name + " doof")
    else:
        print (name + " super")

telbuch = {"Egon":12345, "Paula": 12312312, "Mery": 21323213}
l = []

for i in telbuch.keys():
    l.append((i, telbuch[i]))

print l
