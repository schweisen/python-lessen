import les_15_functies_opdrachten

jouw_soort = les_15_functies_opdrachten.krijg_soort()
computer_soort = les_15_functies_opdrachten.krijg_soort()
jouw_getal = les_15_functies_opdrachten.krijg_getal()
computer_getal = les_15_functies_opdrachten.krijg_getal()

print("Jouw kaart is :", jouw_soort + " " + jouw_getal)
print("De kaart van de computer is :", computer_soort + " " + computer_getal)

jouw_cijfer = int(jouw_getal.replace("aas", "14").replace("koning", "13").replace("dame", "12").replace("boer", "11"))
computer_cijfer = int(computer_getal.replace("aas", "14").replace("koning", "13").replace("dame", "12").replace("boer", "11"))

if jouw_cijfer > computer_cijfer:
    print("Jij wint!")
elif jouw_cijfer < computer_cijfer:
    print("De computer wint!")
else:
    print("Gelijkspel!")
