import random

worp_totaal = 0
worp = 0

# Probeer zo hoog mogelijk totaal te werpen met een dobbelsteen voordat je een 1 gooit.
while worp != 1:
    worp_totaal = worp_totaal + worp
    worp = random.randint(1,6)
    print("Je hebt een " + str(worp) + " gegooid.")
else:
    print("Je worp totaal was " + str(worp_totaal))