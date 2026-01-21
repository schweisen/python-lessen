# Algoritme

Algoritme = herhaalbaar proces om een taak te uitvoeren of probleem op te lossen.

Een algoritme moet geen programma zijn, het is zelfs omgekeerd, een programmeur gaat eerst nadenken over wat zijn programma moet kunnen, welke taak het algoritme moet doen, of welk probleem het moet oplossen. Pas als tweede stap zal er code geschreven worden om dit probleem op te lossen.

Er is niet één correct antwoord om een probleem op te lossen en dus ook niet een perfect algoritme voor elk probleem.

Bijvoorbeeld: jij en een vriend(in) zoeken hetzelfde filmpje op Youtube, je geeft exact dezelfde woorden in maar krijgt toch verschillende opties voor filmpjes. Dit komt omdat het algoritme achter Youtube jullie profiel herkent als verschillend van elkaar.

Bij het ontwerpen of kiezen van een algoritme worden drie eigenschappen in rekening gebracht:

    1. Correctheid van het antwoord
    2. Efficiëntie
    3. Leesbaarheid

Bijvoorbeeld:

Je gaat opzoek naar een filmpje dat je meer uitleg geeft over wat een algoritme is. Ga je hiervoor zoeken op google, YouTube, Instagram, Wikipedia, tiktok, … op de meeste van deze plaatsen ga je een correct en duidelijk filmpje vinden maar toch heb je meteen een voorkeur voor welke website en dus welk achterliggend algoritme je gaat gebruiken. Waarom? We bekijken de drie criteria:

1. Wikipedia toont geen filmpjes, maar legt natuurlijk wel uit in woorden wat een algoritme is, de andere zullen zeker allemaal een correct antwoord kunnen geven.

2. Google gebruiken zal ervoor zorgen dat ik nog naar een andere website moet gaan om mijn filmpje te kunnen bekijken. De filmpjes op tiktok of Instagram zijn eerder kort en zullen misschien te snel gaan om echt te begrijpen wat er uitgelegd wordt.

3. Google toont titels van filmpjes, Instagram en tiktok tonen een thumbnail maar geen uitleg over waar het filmpje over zal gaan, YouTube geeft een korte beschrijving. Bij tiktok kan ik gemakkelijk verschillende filmpjes bekijken tot ik het juiste vind. Bij YouTube zal ik er beter één kunnen kiezen dat mij de juiste, duidelijke info geeft.


# Booleaanse expressies

Om twee waarden te vergelijken gebruiken we vergelijkingsoperatoren, hieronder deze operatoren.

|operator|vergelijking|voorbeeld|vraagt|
|-|-|-|-|
|==|Gelijkheid|x == y|is x gelijk aan y?|
|!=|Ongelijkheid|x != y|is x niet gelijk aan y?|
|<|Minder|x < y|is x minder dan y?|
|<=|Minder dan of gelijk aan|x <= y|is x minder dan of gelijk aan y?|
|>|Groter dan|x > y|is x groter dan y?|
|>=|Groter dan of gelijk aan|x >= y|is x groter dan of gelijk aan y?|

Hoe gebruiken we deze?

    Bijvoorbeeld:

        gebruikersnaam = input("kies een gebruikersnaam: ")

        # gebruikersnaam moeten minstens één karakter lang zijn.
        is_leeg = username == ""
        print("Is je gebruikersnaam leeg? " + str(is_leeg))

Opgepast: datatypes zijn ook hier belangrijk.
Ik kan geen twee datatypes vergelijken.
|Voorbeelden:| |
|-|-|
|“24” == 24 | Dit is altijd False want een string is nooit gelijk aan integer|
|Hallo <= 8 | Zal een error geven want een string kan niet kleiner of groter zijn.|
|“Boom” >= ”aap”|Dit is true want strings worden alfabetisch gerangschikt en a komt voor b en de aap|


# If-statement

Booleaanse expressies staan ons toe om vragen te stellen in ons programma. Als we willen dat het programma iets anders doet als het antwoord True of False is gaan we een “conditional” of voorwaardelijke uitdrukking nodig.

Bv:

    aantal_punten >= 5

    Ik wil dat als het antwoord True is het programma geslaagd zegt, en als ² het antwoord false is, het programma gebuisd zegt.

We beginnen:

    if aantal_punten >= 5:

Dit zegt als aantal_punten True is doe dan wat er achter de : staat. Wat er hier achter staat is echter altijd op de volgende lijn met een insprong of tab. Dus:

    if aantal_punten >= 5:
        Print(“je bent geslaagd”)

Niet zo:

    if aantal_punten >= 5:
    print(“je bent geslaagd”)

Als de booleaanse expressie false is willen we iets anders, dat zetten we eronder zonder insprong.

    if aantal_punten >= 5:
        print(“je bent geslaagd”)
    print(“je bent niet geslaagd”)

Dit gaat natuurlijk nog geen antwoord geven want we hebben geen waarde gegeven aan aantal_punten, dus om volledig te zijn:

    aantal_punten = int(input(“wat is het resultaat op je toets?”))
    if aantal_punten >= 5:
        print(“je bent geslaagd”)
    print(“je bent niet geslaagd”) 