# vraag 5
prijs = 4.25
leeftijd = int(input("Wat is je leeftijd? "))

if leeftijd < 5:
    print("Je mag gratis met de metro rijden.")

if 5 < leeftijd < 60:
    print("Je moet €" + str(prijs) + " betalen.")

if leeftijd > 60:
    print("Je moet €" + str(prijs - 1) + "betalen.")

#############################################################################

prijs = 4.25
leeftijd = int(input("Wat is je leeftijd? "))

if leeftijd < 5:
    print("Je mag gratis met de metro rijden.")

if leeftijd > 5 and leeftijd < 60:
    print("Je moet €" + str(prijs) + " betalen.")

if leeftijd > 60:
    print("Je moet €" + str(prijs - 1) + " betalen.")

#############################################################################

prijs = 4.25
leeftijd = int(input("Wat is je leeftijd? "))

if leeftijd < 5:
    print("Je mag gratis met de metro rijden.")

elif leeftijd < 60:
    print("Je moet €" + str(prijs) + " betalen.")

else:
    print("Je moet €" + str(prijs - 1) + " betalen.")