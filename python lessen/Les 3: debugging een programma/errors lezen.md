# Errors lezen

We hebben al gesproken over de verschillende soorten errors die we kunnen tegenkomen tijdens het programmeren (syntax, runtime en logic) en één fout opsporen is gemakkelijk. We gaan echter vaak niet één fout tegenkomen maar verschillende tegelijk in een programma met vele lijnen code. Zoals op de foto hieronder.

Hoe vind ik daar nu mijn fout in terug?

## STAP 1

Input:
```python
print("Python lessen oefening")
print("Juni uitgaven"")
print("----------")

#een verjaardagstaart en een nieuw toetsenbord gekocht voor Lina.
print("random uitgaven")
print(34.00) + print(22.44)


#uitgaven voor ontbijt, schoolspullen en nutsvoorzieningen.
print("week 1 uitgaven")
print(42.99 + 123.32 + 208.05)

print(week 2 uitgaven)
 print(58.93 + 4.04 + 18.412)

print("week 3 uitgaven")
print(81.50 + 22.12 + 371.33)
```
Output:

```python
file "C:\users\arthur\PycharmProjects\school\les_3.py", line 2 print("Juni uitgaven"")
                     ^
SyntaxError: unterminated string literal (detected at line 2)
```

De output geeft een error, maar wat staat daar?

Het eerste deel noemen we een traceback. Dit vertelt ons waar ons programma staat en waar de error in ons programma staat. We zien hier in het blauw de locatie op mijn computer en als tweede, in dat bestand dat op lijn 2 een probleem is. Het pijltje (^) toont ons zelf waar de error ongeveer zal zijn.

Het tweede deel legt uit welke soort error we getypt hebben. In dit geval een SyntaxError en nog specifieker zegt de error iets over een string op lijn 2.

We zien op lijn 2 dat de string gesloten wordt met twee “ in plaats van één.

## STAP 2
Input: 
```python
print("Python lessen oefening")
print("Juni uitgaven")
print("----------")

#een verjaardagstaart en een nieuw toetsenbord gekocht voor Lina.
print("random uitgaven")
print(34.00) + print(22.44)


#uitgaven voor ontbijt, schoolspullen en nutsvoorzieningen.
print("week 1 uitgaven")
print(42.99 + 123.32 + 208.05)

print(week 2 uitgaven)
 print(58.93 + 4.04 + 18.412)

print("week 3 uitgaven")
print(81.50 + 22.12 + 371.33)
```
Output:
```python
file "C:\users\arthur\PycharmProjects\school\les_3.py", line 13 print(week 2 uitgaven)
      ^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```
Nu lezen we een nieuwe SyntaxError op lijn 13. Hier geeft de IDE een andere uitleg, de syntax is verkeerd en misschien zijn we een komma vergeten.

Als we naar de pijltjes gaan kijken zien we dat er een fout is bij week 2. We zijn geen komma vergeten maar duidelijk de “” waartussen een string moet staan. 

## STAP 3
Input: 
```python
print("Python lessen oefening")
print("Juni uitgaven")
print("----------")

#een verjaardagstaart en een nieuw toetsenbord gekocht voor Lina.
print("random uitgaven")
print(34.00) + print(22.44)


#uitgaven voor ontbijt, schoolspullen en nutsvoorzieningen.
print("week 1 uitgaven")
print(42.99 + 123.32 + 208.05)

print("week 2 uitgaven")
 print(58.93 + 4.04 + 18.412)

print("week 3 uitgaven")
print(81.50 + 22.12 + 371.33)
```
Output:
```python
file "C:\users\arthur\PycharmProjects\school\les_3.py", line 14 print(58.93 + 4.04 + 18.412)
IndentationError: unexpected indent
```
Er is iets mis op lijn 14, er staat nu geen pijltje om ons te helpen. Maar de uitleg kan ons helpen. Een indentationError met een unxpected indent. Indent is engels voor insprong of deuk. Als we op lijn 14 gaan kijken zien we dat de er een spatie voor de print staat. Python verwacht dat een functie elke keer op het begin van de lijn staat.


## STAP 4
Input: 
```python
print("Python lessen oefening")
print("Juni uitgaven")
print("----------")

#een verjaardagstaart en een nieuw toetsenbord gekocht voor Lina.
print("random uitgaven")
print(34.00) + print(22.44)


#uitgaven voor ontbijt, schoolspullen en nutsvoorzieningen.
print("week 1 uitgaven")
print(42.99 + 123.32 + 208.05)

print("week 2 uitgaven")
print(58.93 + 4.04 + 18.412)

print("week 3 uitgaven")
print(81.50 + 22.12 + 371.33)
```
Output:
```python
Juni uitgaven
----------
random uitgaven
34.0
22.44
Traceback (most recent call last):
    File "C:\users\arthur\PycharmProjects\school\les_3.py", line 7, in <module> 
    print(34.00) + print(22.44)
    ~~~~~~~~~~~~~^~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```
Nu is onze output langer, we hebben een runtime error. De eerste lijnen zijn aanwezig in de output. Lijn 1 tot en met 6 zijn aanwezig op lijn 7 is er een fout, deze staat er dus en de rest erna ook niet.

Er is een TypeError: er is iets mis met de + operator in lijn 7.

Op lijn 5 staat dat we de som van deze uitgaven willen berekenen. We moeten dus de twee getallen optellen. Zoals het er nu staat tellen we de functies op en niet de integers. We moeten dus de + operator binnen de functie zetten.

Print(34.00 + 22.44)

## STAP 5
Input: 
```python
print("Python lessen oefening")
print("Juni uitgaven")
print("----------")

#een verjaardagstaart en een nieuw toetsenbord gekocht voor Lina.
print("random uitgaven")
print(34.00 + 22.44)


#uitgaven voor ontbijt, schoolspullen en nutsvoorzieningen.
print("week 1 uitgaven")
print(42.99 + 123.32 + 208.05)

print("week 2 uitgaven")
print(58.93 + 4.04 + 18.412)

print("week 3 uitgaven")
print(81.50 + 22.12 + 371.33)
```
Output:
```python
Juni uitgaven
----------
random uitgaven
56.44
week 1 uitgaven
374.36
week 2 uitgaven
81.382
week 3 uitgaven
474.95
```
We hebben geen error meer maar de output die we willen, of toch? Er is nog één soort error die we moeten controleren namelijk de logic error. In week 2 waren onze uitgaven €81.382, €0,002 is een hoeveelheid die we niet kunnen uitgeven. Er is dus iets misgelopen, de eerste en de laatste week waren onze uitgaven in de honderden euro’s en in week twee niet. De fout zal dus liggen bij €18.412, het is logischer dat de komma één plaats rechts moet opschuiven en de uitgave €184.12 zal zijn.

Dit geeft ons het uiteindelijke resultaat: 
```python
Juni uitgaven
----------
random uitgaven
56.44
week 1 uitgaven
374.36
week 2 uitgaven
247.09
week 3 uitgaven
474.95
```

Nu is het aan jullie: maak de bookwidget: error lezen in het leerpad