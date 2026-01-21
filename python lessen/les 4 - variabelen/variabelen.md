# Variabelen

Python, en elke programmeertaal werkt lijn per lijn. Als we een programma uitvoeren werkt het één lijn af, vergeet deze en gaat naar de volgende.

Als ik een berekening of tekst of iets anders, een value met andere woorden later terug nodig heb. Kan ik deze opslaan als variabele.

Variabele: een locatie in het geheugen om een value op te slaan voor later.
Iedere variabele heeft dus een unieke naam nodig.

    Bv: aantal_leerlingen = 16
    punt_op_toets = 9.5
    naam = “informatica wetenschappen”

De naam van de variabele moet voldoen aan een paar eisen:

    Afspraak 1: twee woorden in een variabele worden altijd gescheiden door een liggend streepje.
    Afspraak 2: de naam van je variabele is altijd in kleine letters.
    Afspraak 3: het eerste teken in een variabele kan nooit een nummer zijn.
    Afspraak 4: namen kunnen geen belangrijke termen zijn in python zoals print of boolean.

Dus NIET: 

    aantal leerlingen = 16
    of Aantal_Leerlingen = 16
    of AANTAL_LEERLINGEN = 16
    of 44N741 133r11N63N = 16

Als je een value opslaat in een variabele wordt deze bijgehouden tot je het programma sluit of tot je een nieuwe value aan de variabele geeft.

    Bv: aantal_leerlingen = 16
    Aantal_leerlingen = 25

Als ik nu print(aantal_leerlingen) run zal ik 25 krijgen en is de computer het getal 16 vergeten.

Iedere variabele is eigenlijk een map waarin je één value kan steken. Als je een nieuwe waarde in de map steekt zal de vorige er automatisch uit gehaald worden.

Variabelen worden zeer veel gebruikt tijdens het programmeren. Bijvoorbeeld bij een spelletje zoals hieronder getoond. Er wordt bijgehouden welke score je hebt, hoeveel munten je hebt, in welke wereld je bent, hoelang je nog hebt voor de tijd op is en hoeveel levens je nog hebt. Deze value verandert natuurlijk doorheen het spel en hoe ingewikkelder het spel of app of programma wordt, hoe meer variabelen er op hetzelfde moment bijgehouden worden.

Hoe gebruiken we deze variabelen nu, en hoe doen we dat efficiënt? Maak daarvoor het bookwidget “variabelen gebruiken”. 