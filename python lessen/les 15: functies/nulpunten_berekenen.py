def nulpunten(a,b,c):
    """nulpunten berekenen van een tweedegraadsfunctie"""
    import math
    discriminant = ((b**2) - (4 * a * c))
    if discriminant < 0:
        return "Geen reële nulpunten"
    else:
        vierkantswortel_D = abs(math.sqrt(discriminant))
        nulpunt1 = (-b - vierkantswortel_D / (2 * a))
        nulpunt2 = (-b + vierkantswortel_D / (2 * a))
        antwoord = [round(nulpunt1,2), round(nulpunt2,2)]
        return antwoord
    
coefficient_a = int(input("Geef coefficiënt a: "))
coefficient_b = int(input("Geef coefficiënt b: "))
coefficient_c = int(input("Geef coefficiënt c: "))
# Gebruik de functie voor de nulpunten en sla het resultaat op in een variabele
berekende_nulpunten = nulpunten(coefficient_a, coefficient_b, coefficient_c)

# Print de variabele met het resultaat
print("De berekende nulpunten zijn:" + str(berekende_nulpunten))