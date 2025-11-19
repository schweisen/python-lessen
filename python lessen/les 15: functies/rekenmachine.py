import sommen
import nulpunten_berekenen
berekening = input("Wat wil je berekenen?(sommen of nulpunten)")

if berekening == "nulpunten":
    coefficient_a = int(input("Geef coefficiënt a: "))
    coefficient_b = int(input("Geef coefficiënt b: "))
    coefficient_c = int(input("Geef coefficiënt c: "))
    # Gebruik de functie voor de nulpunten en sla het resultaat op in een variabele
    berekende_nulpunten = nulpunten_berekenen.nulpunten(coefficient_a, coefficient_b, coefficient_c)

    # Print de variabele met het resultaat
    print("De berekende nulpunten zijn:" + str(berekende_nulpunten))

elif berekening == "sommen":
    getal1 = int(input("Geef het eerste getal: "))
    getal2 = int(input("Geef het tweede getal: "))
    operatie = input("Welke bewerking wil je uitvoeren? (optellen, aftrekken, vermenigvuldigen, delen) ")
    if operatie == "optellen":
        resultaat = sommen.optellen(getal1, getal2)
    elif operatie == "aftrekken":
        resultaat = sommen.aftrekken(getal1, getal2)
    elif operatie == "vermenigvuldigen":
        resultaat = sommen.vermenigvuldigen(getal1, getal2)
    elif operatie == "delen":
        resultaat = sommen.delen(getal1, getal2)
    print("Het resultaat is: " + str(resultaat))