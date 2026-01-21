# user input
Iedereen gebruikt bijna dagelijks een programma, op de computer, de gsm, smartwatch of iets anders. Elk van deze programma’s luisteren naar hun gebruiker (user), je gsm doet pas iets als jij op het scherm tikt.

Elke vorm van actie die een persoon doet die een programma registreert noemen we input. We geven data, op welke manier dan ook aan het programma, om iets mee te doen.

Hoe kunnen we nu input krijgen in Python?

Heel simpel, met de input-functie: 
```python
1.  input()
```

Als we dit runnen zal er bij de output een balkje komen waar je kunt typen. Eens je getypt hebt wat je wilt, druk je op enter en verdwijnt het getypte en eindigt de run. Om de input te kunnen zien moeten we ook weer print gebruiken.

```python
1.  print(input())
```

We kunnen input vragen aan de gebruiker, maar welke? Als je niet het juiste typt krijg je niet het juiste antwoord. De functie input maakt het gemakkelijk om dit te doen door tekst toe te voegen aan je functie.

Input:
```python
1.  print(input("Hoeveel broers en zussen heb je? "))
2.  print("ik heb " + input("hoeveel broers en zussen heb je? ") + " broers en zussen")
```
Output:
```python
hoeveel broers en zussen heb je? 5
hoeveel broers en zussen heb je? 5
ik heb 5 broers en zussen
```
We zien hierboven op lijn dat ik een string heb toegevoegd aan de input functie die getoond wordt als vraag voor welke input je wilt.

Op lijn twee zien we dat het ook mogelijk is om een string toe te voegen aan de print functie die pas getoond wordt nadat de input gegeven is.

Als ik niet iedere keer opnieuw om deze input wil vragen kunnen we deze ook opslaan in een variabele om deze later te gebruiken.

Bv: 
Input:
```python
1.  familie = input("hoeveel broers en zussen heb je? ")
2.  familie = familie
3.  print(familie)
4.  print("ik heb " + familie + " broers en zussen")
5.  print(int(familie)/2)
```
Output:
```python
hoeveel broers en zussen heb je? 2
2
ik heb 2 broers en zussen
1.0
```
Als we een input gaan opslaan kunnen we daar later verschillende dingen mee doen. Dit wordt gebruikt in de meeste programma’s.

## Front-end en back-end

Input typen in onze IDE is natuurlijk nog niet hetzelfde als een spelletje spelen of betalen in de winkel met onze bankkaart. Toch werkt dit op dezelfde manier. Het ziet er alleen niet zo uit.

Wat wij in deze lessen aan het leren zijn noemen we de backend. Dat wil zeggen hoe het programma werkt, wat de logica doet, wat we willen bereiken.
Input typen in onze IDE is natuurlijk nog niet hetzelfde als een spelletje spelen of betalen in de winkel met onze bankkaart. Toch werkt dit op dezelfde manier. Het ziet er alleen niet zo uit.

Wat wij in deze lessen aan het leren zijn noemen we de backend. Dat wil zeggen hoe het programma werkt, wat de logica doet, wat we willen bereiken.

|back-end|front-end|
|:--------:|:---------:|
|Hoe het programma werkt|Hoe het programma er uit ziet|


Deze moeten beiden juist en duidelijk werken. Als de logica niet klopt kan ik het spel niet spelen maar als het spel er niet uitziet zal niemand het willen spelen.

Youtube bijvoorbeeld bestaat al sinds het jaar 2005. De website is in al die jaren door vele miljoenen mensen gebruikt geweest. Ze doet sinds het begin nog steeds hetzelfde: filmpjes opslaan en tonen aan iedereen. De backend is dus in essentie niet heel erg veranderd maar het front-end zeker wel zoals je hier (https://www.youtube.com/watch?v=7xVzQXPepo8) kunt zien. De website van 2006 zouden we vandaag niet meer willen gebruiken. Zowel de back- en front-end zijn dus essentieel bij het maken van een programma. 

Wij gaan natuurlijk eerst verder met de back-end om iets te kunnen maken, dan pas iets moois te kunnen maken.