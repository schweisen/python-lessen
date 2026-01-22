import random

def trek_kaart():
    """Ik trek random een appel of een banaan-kaart."""
    soorten = ["appel","banaan","giftige appel"]
    return random.choice(soorten)

def trek_hand(aantal_kaarten):
    """Geeft de speler het aantal kaarten dat hij vraagt."""
    hand = ""
    for kaart in range(0, aantal_kaarten):
        hand += trek_kaart() + " "
    return hand

def krijg_appel_score(aantal_appels, heeft_giftige_appel):
    """Berekent de score van het aantal appelkaarten."""
    if heeft_giftige_appel is True:
        return aantal_appels * -2
    elif heeft_giftige_appel is False:
        return aantal_appels * 2

def krijg_banaan_score(aantal_bananen):
    """Berekent de score van het aantal bananenkaarten."""
    # bananen zijn meer waard als ze met meer zijn.
    if aantal_bananen == 1:
        return 1
    elif aantal_bananen == 2:
        return 4
    elif aantal_bananen >= 3:
        return 10
    else:
        return 0

def bereken_score(aantal_appels, aantal_bananen, heeft_giftige_appel):
    """Berekent de totale score van de speler."""
    appel_score = krijg_appel_score(aantal_appels, heeft_giftige_appel)
    banaan_score = krijg_banaan_score(aantal_bananen)
    return appel_score + banaan_score

aantal_kaarten = int(input("Hoeveel kaarten wil je trekken? "))
aantal_appels = int(input("Hoeveel appelkaarten heb je getrokken? "))
aantal_bananen = int(input("Hoeveel bananenkaarten heb je getrokken? "))
heeft_giftige_appel = input("Heb je een giftige appelkaart getrokken? (ja/nee) ")
if heeft_giftige_appel.lower() == "ja":
    heeft_giftige_appel = True
else:
    heeft_giftige_appel = False
if aantal_kaarten != aantal_appels + aantal_bananen + (1 if heeft_giftige_appel else 0):
    print("Fout: het totaal aantal kaarten komt niet overeen met de som van appel-, banaan- en giftige appelkaarten.")
else:
    print("Je score is: " + str(bereken_score(aantal_appels, aantal_bananen, heeft_giftige_appel)))