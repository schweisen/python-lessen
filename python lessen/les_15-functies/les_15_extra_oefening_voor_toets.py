def bereken_totaal(pizzas, kms, is_vip):
    """Berekent de totaalprijs van de bestelling."""
    pizza_kost = krijg_pizza_kost(pizzas)
    delivery_kost = krijg_levering_kost(kms, is_vip)

    return pizza_kost + delivery_kost

def krijg_pizza_kost(num_pizzas):
    """Geeft de prijs gebaseerd op het aantal pizza's (stapelkorting!)."""
    # Meer pizza's = goedkoper per stuk.
    if num_pizzas == 1:
        return 12  # 1 pizza is duur
    elif num_pizzas == 2:
        return 20  # 2 voor 20 euro
    elif num_pizzas >= 3:
        return num_pizzas * 9 # Vanaf 3 pizza's zijn ze 9 euro per stuk
    else:
        return 0

def krijg_levering_kost(kms, is_vip):
    """Berekent de bezorgkosten op basis van kilometers."""
    return kms * 2 # Standaard 2 euro per kilometer

# Bereken de rekening voor twee klanten.
bestelling_totaal = bereken_totaal(2, 5, True)
print("Rekening: \n    de klant betaald: \n    " + str(bestelling_totaal) + " euro.")
