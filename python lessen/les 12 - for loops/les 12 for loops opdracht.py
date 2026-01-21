import random

aantal_kassiers = 1

wachtend_om_te_bestellen = 0
wachtend_op_eten = 0
# Klanten komen iedere minuut aan komen in de lijn te staan.
wachtend_om_te_bestellen = wachtend_om_te_bestellen + random.randint(0, 6)

# elke kassier kan tot drie bestellingen per minuut opnemen
nieuwe_bestellingen = min(aantal_kassiers * 3, wachtend_om_te_bestellen)

# Na bestellen wachten klanten tot hun voedsel gemaakt is.
wachtend_om_te_bestellen = wachtend_om_te_bestellen - nieuwe_bestellingen
wachtend_op_eten = wachtend_op_eten + nieuwe_bestellingen

print(str(wachtend_om_te_bestellen) + " klanten wachten op hun bestelling.")
print(str(wachtend_op_eten) + " klanten wachten op hun voedsel.")
