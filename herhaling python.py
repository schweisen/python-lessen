stappen = int(input("Hoeveel stappen heb je vandaag al gezet? "))
if stappen >= 10000:
    print("Goed gedaan!")
else:
    print("Je moet vandaag nog " + str(10000 - stappen) + " stappen zetten.")

calorie = int(input("Hoeveel calorieën heb je gegeten? "))
if calorie < 1800:
    print("Dat is te weinig, je moet iets meer eten.")
elif calorie > 1800 and calorie < 2500:
    print("Goed bezig, dit is een gezond dieet.")
elif calorie > 2500:
    print("Dat is te veel probeer op te passen met wat je eet.")