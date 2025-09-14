# Rekenkundige expressies
We hebben al geleerd wat een operator is. Maar we hebben er tot nu maar één gebruikt de plus operator. Elke operator werkt op dezelfde manier: een waarde, een operator, en een waarde. En elke waarde is een integer of een float.

Er zijn in python een heleboel operatoren. Hieronder vind je een kort overzicht.

|Operator|Operatie|Voorbeeld|Te lezen als|
|--------:|:--------:|:---------:|------------|
|+|Optelling|x + y|Tel x en y bij elkaar op|
|-| Aftrekking|x - y|Trek y van x af|
|*|Vermenigvuldiging|x * y|Vermenigvuldig x en y|
|**|Machtsverheffing|x ** y|X tot de macht y|
|/|Kommadeling|x / y|Deel x door y, geeft een kommagetal|
|//|Vloerdeling|x // y|Deel x door y, geeft een geheel getal, rondt altijd af naar onder|
|%|Modulus (restwaarde)|x % y|Geeft de rest bij de deling van x door y|

De eerste zijn niets nieuws. Ook de machtsverheffing en de kommadeling zouden geen probleem mogen vormen om te gebruiken in python.

Op de twee laatste operatoren gaan we dieper ingaan aangezien deze nieuw zijn en tijdens het programmeren zeer veel worden gebruikt.

## Vloerdeling
Bij een kommadeling is de uitkomst altijd een float.
    
    Bv: 6 / 4 = 1.5
    6 / 3 = 2.0
Of de .0 getoond wordt of niet, voor python is de uitkomst altijd een float. Bij een vloerdeling is de uitkomst altijd een integer. Een vloerdeling beantwoord dus de vraag:

Hoeveel keer past de deler in het deeltal?

    Bv: 6 // 4 = 1
Het antwoord is dus niet 2, er wordt altijd naar beneden afgerond bij een vloerdeling. Of anders gezegd: 4 past één keer 6. 
## Modulus
De modulus is het omgekeerde van de vloerdeling. Dit geeft ons de rest bij een deling. Het beantwoordt dus de vraag:

Wat blijft er over bij een deling?

    Bv: 6 % 4 = 2

Het antwoord is dus niet 0.5 maar 2 want 4 past één keer in 6 en dan blijft er nog 2 over van de 6.

Dit is duidelijker als we een staartdeling gebruiken als voorstelling.

    Kommadeling:    6 / 4 = 1.5
    Vloerdeling:    6 // 4 = 1
        Modulus:    6 % 4 = 2

## De repeterende breuk
Bij een deling krijgen we soms een eindeloos repeterend deel.

    Bv: 1 / 3 = 0.3333333333…

In Python krijgen we dit echter op onverwachte momenten, hoe komt dat?
    
    Bv: 1.48 + 1.24 = 2.72
In Python is het echter:
```python
Input:
print(1.48 + 1.24)

Output:
2.71999999999999999999999999999999
```
Python rekent niet in het decimaalstelsel zoals wij dat doen maar zoals alle computers wordt er in binair gerekend. Dit zorgt ervoor dat het herhalende deel niet altijd voorkomt waar wij het zouden verwachten. Schrik dus niet als je dit tegenkomt bij een operatie waar je het niet verwacht.

Wil je bepalen hoeveel getallen na de komma er getoond worden? Dan gebruiken we de functie round()
bv: 

    round(1.48 + 1.24, 2)   zal afronden op twee cijfers na de komma
    round(1.48 + 1.24, 4)   zal afronden op vier cijfers na de komma 

## Operatoren bij strings

Bij strings werken deze operatoren natuurlijk niet. Enkel de + operator is bruikbaar bij strings. Als je een van de andere operatoren gebruikt bij een string krijg je een error: TypeError: unsupported operand type(s) for /: ‘str’ and ‘str’

Er is één uitzondering * strings kunnen wel vermenigvuldigd worden.

    Bv: 3 * ”ha” = hahaha

Een string vermenigvuldigen herhaald de string zoveel keer.

## Type casting
Soms willen we een string optellen bij een float.

    Bv: print(“het resultaat van je toets is: “ + 8.5)

Dit zal een TypeError geven, want de computer wilt geen string en float optellen. Maar wij willen dit wel optellen of toch samen tonen. Om dit te doen zullen we moeten typecasten of soort gieten in het Nederlands. Typecasting betekent dat we een waarde van het ene datatype in het andere veranderen.

|Functie|Output|
|------|-----|
|Str() | De output is een string |
|Int() | De output is een integer |
|Float() | De output is een float |
|Bool() | De output is een boolean |

Hierbij zijn een aantal belangrijke bemerkingen.

1. Eerste bemerking: Als je iets wilt typecasten dat nergens opslaat zal je een ValueError krijgen.

    Bv: int(“5.5”) is onmogelijk

Je kunt 5.5 namelijk niet omzetten in een geheel getal.

2. Tweede bemerking: de input functie zal altijd een string opslaan.
    Bv:
```python
spel = input(“kies een getal tussen 0 en 9: ”)
print(spel / 2)
#geeft een error.
Print(int(spel) / 2)
#zal wel werken
```
Je kunt ook de input meteen typecasten:
```python
spel = int(input(“kies een getal tussen 0 en 9: ”))
```
3. Derde bemerking: een float naar een integer typecasten.

    Bv: int(3.8)

Dit doet wat een vloerdeling ook doet. Het knipt de decimalen eraf, het neemt het kleinste gehele getal. In dit geval dus:

    Int(3.8) = 3 