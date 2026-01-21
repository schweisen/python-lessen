# break en continue
Soms willen we een loop aanpassen om onder bepaalde condities vroeger te stoppen of één loop over te slaan en meteen opnieuw te beginnen.

## Break (pauze)
Om meteen een loop stop te zetten. voegen we het woord break toe. Zoals je ziet in het onderstaande voorbeeld, de loop zal 100 keer lopen. Als we een break toevoegen zal het echter maar één keer lopen.

bijvoorbeeld:
```python
for i in range(100):
    print(str(i) + " voor break")
    print(str(i) + " na break")

print("buiten de loop")
```
```python
for i in range(100):
    print(str(i) + " voor break")
    break
    print(str(i) + " na break")

print("buiten de loop")
```

Dit maakt het tweede deel van de code natuurlijk volledig overbodig, de na de break zal nooit geprint worden. Meestal zal de break dus onder een conditionele voorwaarde geplaatst worden zoals in het onderstaande voorbeeld, de loop zal hier tien keer lopen voordat de break gelezen wordt en het loop stopt.

bijvoorbeeld:
```python
for i in range(100):
    print(str(i) + " voor break")
    if i == 10:
        break

    print(str(i) + " na break")

print("buiten de loop")
```
Het bovenstaande voorbeeld is duidelijk maar niet heel realistisch waarom zou ik een loop maken die 100 keer loopt om hem dan na tien keer al af te breken.
Hieronder een realistischer voorbeeld:

```python
correct_password = "geheim123"

for poging in range(3):
    wachtwoord = input("Geef je wachtwoord in: ")

    if wachtwoord == correct_password:
        print("Wachtwoord correct. Toegang verleend.")
        break  # we stoppen zodra het wachtwoord correct is

    print("Wachtwoord fout. Probeer opnieuw.")

print("Einde programma.")
```
## continue (ga verder met de loop)
Continue zorgt ervoor dat de loop niet verder loopt maar meteen opnieuw begint vanaf nul.

bijvoorbeeld:
```python
for i in range(100):
    print(str(i) + " voor break")
    continue
    print(str(i) + " na break")

print("buiten de loop")
```
Hier gaat de code opnieuw beginnen na 'voor break' geprint te hebben. Dit is, net zoals bij een break op deze manier niet erg nuttig. Ook een continue krijgt meestal zijn eigen conditionele voorwaarde zoals in het voorbeeld hieronder:

bijvoorbeeld:
```python
for i in range(100):
    print(str(i) + " voor break")
    if i == 10:
        print("continue")
        continue
    print(str(i) + " na break")

print("buiten de loop")
```
Of een meer realistischere reden om een continue te gebruiken:

bijvoorbeeld:
```python
score = 0

for i in range(5):
    antwoord = input("Wat is 2 + 2? ")

    if antwoord != "4":
        print("Fout antwoord. Andere vraag...")
        continue

    print("Juist antwoord!")
    score += 1

print("Je eindscore is: " + str(score))
```