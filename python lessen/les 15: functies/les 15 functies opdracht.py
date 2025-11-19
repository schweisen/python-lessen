uren_gespeeld = 15

if uren_gespeeld >= 50:
    trofee_naam = "Veteran"
elif uren_gespeeld >= 10:
    trofee_naam = "Adventurer"
else:
    trofee_naam = "Beginner"

print(trofee_naam)