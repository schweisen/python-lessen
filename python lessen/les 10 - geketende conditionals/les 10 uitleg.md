## Geketende conditionals
We hebben gesproken over if en else en kunnen dankzij samengestelde booleaanse voorwaarden de computer uit verschillende keuzes laten kiezen. 

Bv:
```python
punt_op_toets = float(input("Wat  is de score van de toets op 10? "))

if punt_op_toets < 5:
  print("Je bent niet geslaagd.")
  kleur_resultaat = "rood"

if 5 <= punt_op_toets < 7:
  print("Je bent geslaagd op voldoende wijze.")
  kleur_resultaat = "groen"

if punt_op_toets >= 7:
  print("Je bent geslagd met onderscheiding.")
  kleur_resultaat = "donkergroen"
```
---
Dit is correct en volledig maar het kan beter. De drie if-statements worden iedere keer apart bekeken. Voor ons kleine programma is dat geen probleem maar een groter programma wordt trager hoe meer lijnen er gelezen moeten worden.

Er bestaat een manier om dit efficiënter en beter te doen. Daarvoor gebruiken we het elif-statement. Een combinatie van if en else. We kunnen ons programma dan opnieuw schrijven op onderstaande manier.

Bv:
```python
punt_op_toets = float(input("Wat is de score van de toets op 10? "))

if punt_op_toets < 5:
  print("Je bent niet geslaagd.")
  kleur_resultaat = "rood"

elif 5 <= punt_op_toets < 7:
  print("Je bent geslaagd op voldoende wijze.")
  kleur_resultaat = "groen"

else:
  print("Je bent geslagd met onderscheiding.")
  kleur_resultaat = "donkergroen"
```
---
Dit zal dezelfde correcte uitleg geven als het eerste programma maar op een veel efficiëntere manier.

Else wordt enkel uitgevoerd als de if-voorwaarde False is. Hetzelfde is waar voor Elif.

Dus bv: als je 4/10 haalt op je toets is lijn 3 = True en worden lijn 7 en 11 dus overgeslagen en het programma eindigt meteen.

Dit maakt het programma een stuk efficiënter en dus correcter.

Een voorbeeld van hoe een programma efficiënter wordt dankzij de geketende conditional, gebruikmakende van if-elif-else: 

```python
dag_van_de_week = input("Welke dag van de week is het?" )

if dag_van_de_week == "zaterdag" or dag_van_de_week == "zondag":
  print("We zijn enkel open van 11 tot 14 uur vandaag.")

if dag_van_de_week == "maandag":
  print("We zijn gesloten vandaag.")

if (
  dag_van_de_week == "dinsdag"
  or dag_van_de_week == "woensdag"
  or dag_van_de_week == "donderdag"
  or dag_van_de_week == "vrijdag"
):
  print("We zijn open van 9 tot 15 uur.")
```
---
 of gebruikmakend van if-elif-else:

 ```python
dag_van_de_week = input("Welke dag van de week is het?" )

if dag_van_de_week == "zaterdag" or dag_van_de_week == "zondag":
  print("We zijn enkel open van 11 tot 14 uur vandaag.")

elif dag_van_de_week == "maandag":
  print("We zijn gesloten vandaag.")

else:
  print("We zijn open van 9 tot 15 uur.")
```
---
Niet alleen is deze tweede optie 5 lijnen korter om hetzelfde te zeggen. Het is ook gemakkelijker te volgen als programmeerder. Op deze manier zijn we veel sneller zeker dat de opties elkaar niet overlappen of er geen voorwaarde gemist is.

## Elif-gebruiken en conditionals opstellen
Waarvoor kunnen we dit gebruiken?

### 1 Een bereik vastleggen.

We kunnen de volgorde van code gebruiken in ons voordeel. De computer leest de volgende elif pas als de vorige False was.

Bv: het eerste voorbeeld kan nog efficiënter:

```python
punt_op_toets = float(input("Wat is de score van de toets op 10? "))

if punt_op_toets < 5:
  print("Je bent niet geslaagd.")
  kleur_resultaat = "rood"
elif punt_op_toets < 7:
  print("Je bent geslaagd op voldoende wijze.")
  kleur_resultaat = "lichtgroen"
elif punt_op_toets < 8:
  print("Je bent geslaagd met onderscheiding.")
  kleur_resultaat = "groen"
else:
  print("Je bent geslaagd met grote onderscheiding.")
  kleur_resultaat = "donkergroen"
```
---
Dankzij elif moeten geen bereik geven ook al is 4 kleiner dan 5, 7 en 8. Zodra lijn 3 True is zal de rest niet meer gelezen worden door de computer. 

### 2 een input valideren
We willen vaak controleren of de input overeenkomt met een voorwaarde, of het wachtwoord juist is bijvoorbeeld. Enkel als dat zo is willen we met deze waarde iets doen.

Bv: 
```python
bestandsnaam = input("Hoe wil je het bestand noemen? ")

if len(bestandnaam) < 3 or len(bestandnaam) > 20:
  # Verwijder de bestandnaam als ze ongeldig is.
  bestandnaam = ""
  print("De bestandnaam moet tussen 3 en 20 tekens lang zijn.")
else:
  #Foto's worden opgeslagen als JPEGs, dus voegen we een extensie toe aan het bestand.
  bestandnaam = bestandnaam + ".jpeg"
  print("Het bestand is hernoemd naar " + bestandnaam)
```
---
### 3 een waarde overschrijven
We kunnen een variabele veranderen afhankelijk van een voorwaarde. Bij dit soort toepassing laten we vaak de else weg omdat else meestal zal zijn dat we de waarde niet willen laten veranderen. 
```python
voertuig : input("Kies een voertuig: ")

snelheid = 5
versnelling = 5

#Spelers krijgen een mega voertuig door een race te winnen op elk parcour.
if voertuig == "mega cycle":
  versnelling = versnelling + 4
elif voertuig == "mega kart":
  snelheid = snelheid + 2
  versnelling = versnelling + 2

print(
  "Het " + voertuig + " heeft " + str(snelheid) + " snelheid en " + str(versnelling) + " versnelling."
)
```
---
Het opstellen van een juiste ketting aan condities is essentieel om de juiste uitkomst te krijgen.

Hierop zullen we nu oefenen.