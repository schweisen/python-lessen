## Code reviewen
 Een goed programma schrijven is niet alleen een kwestie van code laten werken, maar ook van samenwerken en verbeteren. Een probleem kan op meerdere manieren opgelost worden en code wordt vaak door meerdere mensen geschreven. Om te zorgen dat iedereen de code begrijpt en kan verbeteren, is een code review belangrijk. Dit helpt om fouten te vinden, prestaties te verbeteren en de code leesbaar en onderhoudbaar te maken. Hier leggen we 4 principes uit die we hanteren bij het optimaliseren van code.

In het engels noemen dit het DRY-principe (Don’t Repeat Yourself)

### 1. Vergelijk geen booleaans direct (Don't Compare booleaans)
Een veelvoorkomende fout is het rechtstreeks vergelijken van een booleaanse waarde met True of False. Dit is onnodig en maakt de code minder leesbaar. Booleanen zijn al True of False op zichzelf, en een expliciete vergelijking voegt alleen ruis toe. 

JUIST
```python
if is_ingelogd:
    print("Welkom!")
```
FOUT
```python
if is_ingelogd == True:
    print("Welkom!")
```
---
In het eerste voorbeeld is de voorwaarde kort en duidelijk. In het foute voorbeeld wordt een overbodige vergelijking gemaakt.

### 2. hergebruik gedeelde logica (Up-level shared logic)
Als meerdere delen van je code dezelfde logica herhalen, is het beter om deze logica op een hoger niveau te plaatsen. Dit voorkomt duplicatie en maakt de code beter onderhoudbaar. 

FOUT
```python
if leeftijd >= 18:
    print("Je mag stemmen.")
if leeftijd >= 18:
    print("Je mag alcohol kopen.") 
```
JUIST
```python
if leeftijd >= 18:
    print("Je mag stemmen.")
    print("Je mag alcohol kopen.") 
```
---
In de juiste versie staat de gedeelde voorwaarde op één plaats, wat de code korter en overzichtelijker maakt. 

### 3. Combineer gerelateerde branches (combine related branches)
Soms bevatten if-structuren meerdere voorwaarden die nauw met elkaar verbonden zijn. Het combineren van deze branches kan de leesbaarheid verbeteren. 

FOUT
```python
if status == "actief":
    print("Gebruiker is actief.")
else:
    if status == "inactief":
        print("Gebruiker is inactief.") 
```
JUIST
```python
if status == "actief":
    print("Gebruiker is actief.")
elif status == "inactief":
    print("Gebruiker is inactief.") 
```
---
Door elif te gebruiken, wordt de code directer en vermijd je geneste if-structuren.

### 4. Gebruik aaneengeschakelde exclusieve voorwaarden (chain exclusive conditions)
Als een reeks voorwaarden wederzijds exclusief is (ze kunnen niet tegelijkertijd waar zijn), gebruik dan een aaneengeschakelde structuur met elif. Dit maakt de code efficiënter en voorkomt overbodige controles.

FOUT
```python
if score >= 90:
    print("Uitstekend!")
if score >= 75 and score < 90:
    print("Goed gedaan!")
if score >= 50 and score < 75:
    print("Voldoende.")
else:
    print("Onvoldoende.") 
```
JUIST
```python
if score >= 90:
    print("Uitstekend!")
elif score >= 75:
    print("Goed gedaan!")
elif score >= 50:
    print("Voldoende.")
else:
    print("Onvoldoende.")
```
---
De juiste versie voorkomt onnodige vergelijkingen en maakt de structuur duidelijker.

## Overzicht van code review principes
| Stijlregel                             | Beschrijving |
|-----------------------------------------|-------------|
| Vergelijk geen booleans direct         | Booleanen zijn al `True` of `False`, dus vermijd onnodige vergelijkingen. |
| Hergebruik gedeelde logica             | Plaats herhaalde logica op een hoger niveau om duplicatie te voorkomen. |
| Combineer gerelateerde branches        | Gebruik `elif` in plaats van geneste `if`-structuren. |
| Gebruik aaneengeschakelde exclusieve voorwaarden | Gebruik `elif` bij exclusieve voorwaarden om overbodige checks te vermijden. |
