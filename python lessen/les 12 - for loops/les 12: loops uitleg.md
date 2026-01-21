# for-loops
## Wat is het verschil tussen een while-loop en een for-loop?
Vaak willen een loop een aantal keer herhalen, dit doen we door bij de loop-variabele steeds één bij te tellen. Dit kunnen we gemakkelijker en sneller doen door gebruik te maken van een for-loop.

bijvoorbeeld while-loop:

```python
sprongen = 0

while sprongen <= 9:
    print("Je hebt " + str(sprongen) + " sprongen gedaan.")
    sprongen = sprongen + 1
```
bijvoorbeeld for-loop:

```python
for sprongen in range(9):
    print("Je hebt " + str(sprongen) + " sprongen gedaan.")
```
Deze loop herhaalt zich zolang de loop-variabele binnen het bereik, 5 ligt. Daar komt de naam vandaan: 'for as long as the loop-variabele is in the range of 9 run the loop.'
De for-loop is in dit geval een stuk efficiënter, je moet geen loop-variabele definiëren op voorhand en je moet de loop-variabele niet veranderen binnen je loop. Het for-statement en de range() functie lossen dit beiden op.

## for - statement
Het for-statement zal de volgende woorden op dezelfde lijn stap voor stap evalueren tot het opgelost is.

### range() - functie
De range-functie genereerd een aantal waarden tussen een start en stop-waarde met een vast interval.
Automatisch kiest python:
- start-waarde = 0
- interval = 1
- stop-waarde = getal tussen de haakjes, 

In ons voorbeeld zal het sprongen herhalen tot 9, niet tot en met 9, het stopt dus bij 8. het for-statement zorgt ervoor dat de loop-variabele iedere keer gelijkgesteld wordt aan de volgende stap in de range. Bij de eerste stap is de loop-variabele gelijk aan 0, bij de laatste gelijk aan 8.
### De range() - functie aanpassen
We kunnen binnen de haakjes van de range()-functie een extra argument toevoegen. Dit begint met het start-waarde en daarop volgt dan de stop-waarde, daarna kan ook nog het interval aangepast worden.

bijvoorbeeld: bij het eerste voorbeeld start het automatisch bij 0, bij de tweede start het bij 3. Bij de laatste gaat dit vooruit in stappen van 2 dus van 3 naar 5 naar 7, waarna het stopt want 9 ligt buiten het bereik.

```python
#1
for sprongen in range(9):
    print("Je hebt " + str(sprongen) + " sprongen gedaan.")
#2
for sprongen in range(3, 9):
    print("Je hebt " + str(sprongen) + " sprongen gedaan.")
#3
for sprongen in range(3, 9, 2):
    print("Je hebt " + str(sprongen) + " sprongen gedaan.")
```

## Wanneer while- en for-loops gebruiken?
De for-loop is korter, waarom zouden we dan ooit de while-loop gebruiken?
De for-loop werkt enkel als we op voorhand weten hoeveel keer we de loop moeten laten lopen. Ik weet hoeveel adressen er in de lijst staan maar niet hoeveel keer ik moet proberen tot een wachtwoord correct zal zijn.

bijvoorbeeld:
```python
# for-loop
gebruikers = ["alice@voorbeeld.com", "bob@voorbeeld.com", "charlie@voorbeeld.com"]

for gebruikers in gebruikers:
    print("Stuur een email naar " + gebruikers)

# while-loop
correct_wachtwoord = "python123"
wachtwoord = ""

while wachtwoord != correct_wachtwoord:
    wachtwoord = input("geef je wachtwoord: ")
    print("Niet correct, probeer opnieuw: ")
else:
    print("correct ingelogd!")
```
