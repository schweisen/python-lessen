planeet = input("Op welke planeet wil je, je gewicht berekenen? ")

#we meten de zwaartekracht van een planeet in m/s^2
mercurius_gravitatieconstante = 3.7
venus_gravitatieconstante = 8.9
aarde_gravitatieconstante = 9.81
mars_gravitatieconstante = 3.7
jupiter_gravitatieconstante = 23.1
saturnus_gravitatieconstante = 9
uranus_gravitatieconstante = 8.7
neptunus_gravitatieconstante = 11

if planeet in ("Mercurius","Venus","Mars","Jupiter","Saturnus","Uranus","Neptunus"):
    gewicht_aarde = float(input("hoeveel weeg je op aarde (kg)? "))
    massa = gewicht_aarde / aarde_gravitatieconstante
else:
    massa = 0
    print("De planeet: " + planeet + " staat niet in de database, kies een andere.")

#gewicht is massa * zwaartekracht
if planeet == "Mercurius" or planeet == "Mars":
    nieuw_gewicht = massa * mercurius_gravitatieconstante
elif planeet == "Venus":
    nieuw_gewicht = massa * venus_gravitatieconstante
elif planeet == "Jupiter":
    nieuw_gewicht = massa * jupiter_gravitatieconstante
elif planeet == "Saturnus":
    nieuw_gewicht = massa * saturnus_gravitatieconstante
elif planeet == "Uranus":
    nieuw_gewicht = massa * uranus_gravitatieconstante
elif planeet == "Neptunus":
    nieuw_gewicht = massa * neptunus_gravitatieconstante

if massa != 0:
    print("De persoon zou " + str(round(nieuw_gewicht,2)) + " kg wegen op " + planeet + ".")