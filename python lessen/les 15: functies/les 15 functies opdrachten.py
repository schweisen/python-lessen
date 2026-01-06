# we maken een programma dat een gebruiker een toe laat om verschillende kaartspelen te spelen (poker, hartenjagen, presidenten)
# 1) we maken de functie trek_hand die een aantal random kaarten uit het pak trekt.
# 2) we maken twee functies, één die een soort kiest (schuppen, harten, klaveren, koeken) en één die een getal kiest (1-10+boer, dame en koning)
# 3) we zorgen dat de trek kaart functie die twee vorige functies juist gebruikt.

import random

def trek_kaart():
    """Geeft een random kaart uit het pak als een string."""

def trek_hand(aantal_kaarten):
    """Geeft een speler een aantal random kaarten, nodig om het spel te spelen."""
    hand = ""
    for kaart in range(aantal_kaarten):
        hand += trek_kaart() + "\n"
    return hand

print(trek_hand(5))
