def krijg_score(bananen, appels, heeft_vergiftige_appel):
    """Geeft de totale score van een speler, gebaseerd op het aantal kaarten van elke soort."""
    bananen_score = krijg_banana_score(bananen)
    appel_score = krijg_appel_score(appels, heeft_vergiftige_appel)

    return bananen_score + appel_score

def krijg_banana_score(aantal_bananen):
    """Geeft de score van een speler op basis van het aantal bananen kaarten."""
    # Bananen zijn meer waard in trossen.
    if aantal_bananen == 1:
        return 1
    elif aantal_bananen == 2:
        return 4
    elif aantal_bananen >= 3:
        return 10
    else:
        return 0

def krijg_appel_score(aantal_appels, heeft_vergiftige_appel):
    """Geeft de score van een speler op basis van het aantal appel kaarten."""
    return aantal_appels * 2


# Berekent de totale score voor elke speler.
speler1_score = krijg_score(3, 2, True)
speler2_score = krijg_score(1, 5, False)
print("Scores: speler 1=" + str(speler1_score) + ", speler 2=" + str(speler2_score))
