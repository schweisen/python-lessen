# loops
## Wat is een loop?
Soms willen we in een programma een conditie keer op keer testen. Onze locatie, of een lijst met liedjes waarin we zoeken naar de juiste titel. Om dit niet iedere keer opnieuw te programmeren gebruiken we een loop.
Een loop of lus controleert een booleaanse voorwaarde, opnieuw en opnieuw tot ze False is.
bijvoorbeeld:

```python
stappen = 0

while stappen <= 5:
    print("Je hebt " + str(stappen) + " stappen gezet.")
    stappen = stappen + 1
```
Iedere run door de lus zal je aantal stappen geprint worden en zal er één stap bijkomen. De lus zal blijven lopen tot de variabele stappen groter is dan 5.

## Opbouw van een loop
 Een lus moet een aantal onderdelen bevatten:
 - loop-variabele definieren
 
 Voordat je de loop kunt starten moet de loop-variabele gedefinieerd worden.

 - controleer loop-variabele in conditie

 Om de loop te starten beginnen we met het woord while (terwijl), gevolgd door een booleaanse conditie. zoals bij de if-statements eindigt de lijn met een : (dubbelpunt).
 De booleaanse voorwaarde moet altijd de loop-variabele controleren.

 - update loop-variabele op einde van conditie

 Het laatste onderdeel van de loop moet altijd de update van de loop-variabele zijn. Dit kan op elke manier die je wilt. Maar als dit niet correct gebeurt zal de loop conditie niet veranderen en zal de loop voor altijd doorlopen tot het geheugen van je computer vol zit.

 ## eindigen van een loop
Een loop eindigt automatisch als de booleaanse conditie False wordt. Maar we kunnen hierbij ook een melding geven, gebruikmakend van else. Net zoals bij een if-conditional. We voegen dit toe aan het bovenstaande voorbeeld.

```python
stappen = 0

while stappen <= 5:
    print("Je hebt " + str(stappen) + " stappen gezet.")
    stappen = stappen + 1
else:
    print("Je hebt genoeg gewandeld.")
```
## Waarvoor een loop gebruiken?
### aftellen
We kunnen een loop gebruiken om iedere keer iets af te trekken van onze waarden. Het is dan belangrijk dat onze loop eindigt, wat we doen door naar de stop waarde te evalueren.
bv:
```python
bots_hoogte = 55.5

while bots_hoogte > 1:
    hoogte = round(bots_hoogte, 2)
    print("De bal is op " + str(hoogte) +"cm")
    # De bal verliest iedere keer 30% van zijn hoogte
    bots_hoogte = bots_hoogte * 0.7    
```

### verbeteren van user input
We kunnen een conditie gebruiken om te controleren of een waarde klopt of niet. Maar met een loop kunnen we de waarde verbeteren zodat ze uiteindelijk klopt. Dit wordt bijvoorbeeld gebruikt als je je wachtwoord verkeerd intypt.
bv:
```python
gebruiksnaam = ""

while len(gebruiksnaam) < 5:
    print("Gebruiksnamen moeten minstens 5 karakters bevatten.")
    gebruiksnaam = input("Kies een Gebruiknaam: ")

print("Gebruiksnaam is veranderd.")  
```
