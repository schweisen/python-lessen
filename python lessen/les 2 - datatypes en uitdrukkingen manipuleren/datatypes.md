# Datatypes (IDE)

Alle programma’s manipuleren data op één of andere manier. Dit kan tekst zijn, bijvoorbeeld om het juiste woord op een pagina van Wikipedia te vinden. Of foto’s om gezichten te herkennen. Al deze complexe data bestaat uiteindelijk uit nummers en letters en python verdeelt al deze data in een 15-tal datatypes. We gaan beginnen met een paar simpele datatypes.

## Primitieve datatypes

Één data stukje noemen we een waarde of value in het engels. En het datatype van deze value verteld ons hoe het programma deze value moet interpreteren.

De primitieve datatypes worden zo genoemd omdat we met deze alle ingewikkelde datatypes kunnen opbouwen.

We starten met integers, floats, booleans en strings of in het nederlands gehele getallen, komma getallen, booleanen en strengen.

### Integers (gehele getallen)

Een integer is elk getal zonder komma. Dat betekent dus negatieve, positieve getallen en nul.

    Bv: 5, 3544, 0, 54366843, en -1842387 zijn allemaal integers.

De computer herkent geen punten of komma’s, het is dus 1000000 en niet 1.000.000 of 1,000,000.

### Floats (komma getallen)

Een float is elk komma getal. De naam float of drijvend in het nederlands komt van het idee dat de komma drijft tussen de getallen.
In het Engels, en dus in python, op de computer, is een komma getal genoteerd met een punt.

    Bv: 1.5, 3.141592653, -16.06, -33.3333333 en 69.5 zijn allemaal floats.

Ook de getallen 0.0 en -5.0 en 15.000 zijn allemaal floats. De computer herkent elk getal met een punt tussen als een float, ook als er enkel nullen nakomen.

### Boolean (booleaanse expressie)

Booleans zijn vernoemd naar George Boole, een wiskundige en logicus. Een van de grondleggers van de informaticawetenschappen. Deze naam heeft dus geen vertaling.

Een boolean is een waarheidsuitdrukking, het kan dus slechts twee values hebben: waar of niet waar, of in het Engels True of False.

Bv: staat de computer aan of uit. Is het antwoord op de vraag ja of nee.

In python moeten we True en False schrijven, dat is met hoofdletter. True en false zal de computer niet herkennen als boolean.

### Strings (strengen)

Een string is tekst, of een streng van figuren. Een figuur kan alles zijn wat we kunnen typen op een toetsenbord. Er is slechts één voorwaarde voor een string en dat is dat de figuren omringd worden door quotatietekens.

    Bv: “b”, “SNI”, “hoe laat is het?” en “^$ùµ,;:=”

De values “-8”, “97.6”, “3+6” en “True” zijn allemaal strings. De computer herkent de quotatietekens als een string zelfs als de tekst binnen de quotatietekens een integer, float of boolean zijn.

“” is een lege of empty string, dit is anders dan “ “, want daar staat een spatie in de string.

## Complexe datatypes

Deze simpele datatypes kunnen (bijna) alle soorten data maken. Maar hoe maak ik nu een foto, video of lied of website op basis van deze datatypes?

Denk aan een website? Wat zie je daarop? Misschien heb je een gebruikersnaam? (een string), of een aantal views (een integer), of een prijs (een float). Misschien houdt het bij welke berichten je al gelezen hebt en welke nog niet. (een boolean). Dit hele bestand is eigenlijk één heel lange string.

## Audio en afbeeldingen

Computers stellen alle audio en afbeeldingsdata voor als een lange rij van integers. Een geluidsgolf bestaat bijvoorbeeld uit een heel aantal floats die de tijd aanduiden en daarbij telkens een integer die hoogte van de golf beschrijft.

Van een pixel heb je al wel gehoord. Dit is hoe een computer over video denkt. Elke afbeelding wordt afgebroken in een set van pixels, deze krijgen een coördinaat bestaand uit twee integers zodat we weten waar het staat en nog eens drie integers die van 0 tot 255 gaan en ons vertellen hoeveel rood licht, groen licht en blauw licht er in elk pixel zitten.

Bijvoorbeeld:

De onderstaande foto bestaat uit 18*25 pixels.
We kunnen een pixel zo voorstellen:

    X = 15

    Y = 2

    Rood= 255

    Groen= 255

    Blauw= 2

    Of (15,2,255,255,2)

## Binaire data

Waarom is dit allemaal zo ingewikkeld? Een computer verstaat eigenlijk enkel binair, dat wil zeggen 0 en 1. Alle datatypes die we net besproken hebben wordt door de computer omgezet in deze 0’en en 1’en. Computers kunnen de primitieve types gemakkelijk omzetten in 0 en 1.

    58 = 00110101 00111000

    “p” = 01110000

Als je zelf computertaal wilt spreken, kan dat hier. https://www.convertbinary.com/text-to-binary/

Je zal merken dat één zin meteen heel snel héél lang wordt. En dat is waarom wij niet in 0 en 1 programmeren maar met python als tussenstap.
