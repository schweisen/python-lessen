import random

# Rol twee 6-kantige dobbelstenen.

aantal_worpen = 0
totaal_van_de_worpen = 0
while aantal_worpen != 0:
    eerste_steen = random.randint(1, 6)
    tweede_steen = random.randint(1, 6)
    dobbelsteen_som = eerste_steen + tweede_steen
    print("Je rolde een " + str(dobbelsteen_som) + "!")