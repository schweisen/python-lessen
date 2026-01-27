score = int(input("Hoeveel procent behaalde je? "))

if score < 50:
    print("Niet goed gedaan. ")
    print("Je moet opnieuw studeren")
    if score < 20:
        print("Heb je wel gestudeerd?")
else:
    print("Je bent geslaagd.")
