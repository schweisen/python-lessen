aantal_eieren = int(input("Hoeveel eieren heb je? "))
aantal_dozen = aantal_eieren // 12
eieren_over = aantal_eieren % 12

print("Om al je eieren in dozen te steken zal je " + str(aantal_dozen) + " dozen nodig hebben en nog " + str(eieren_over) + " eieren over hebben.")