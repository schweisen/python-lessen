# Leesbaarheid van de code

Een programma moet leesbaar zijn door iemand die er niet bij was toen het geschreven werd. De meeste programma’s, website en spellen worden gemaakt door verschillende mensen tegelijk. Om een programma leesbaar te houden maken we een aantal afspraken. Dit zijn geen wetten en de code is zeker niet fout zonder maar voor ieders gemak zullen we ons hieraan te houden.

Dit maakt de code leesbaarder, en maakt het gemakkelijker om deze aan te passen en errors te verbeteren.

1. Formateren

AlS We O nZe T eXt O p DeZe Ma Nier Z oUdEn S cHrIjVeN, Bl ijFt H eT Na TuRlIjK Le Es BaAr, M aAr H eT M aAkT H eT E eN St Uk L aNgz AmEr E n MoE i LjKe R O m T e L e Ze N.

Dat is voor code hetzelfde formateren volgens de standaardregels maakt het leesbaarder, als je dit genoeg doet gaat dat automatisch en zullen je hersenen na een tijd weten wat er daarna komt. Dit maakt programmeren gemakkelijker en sneller.

## Naamgeven en documenteren

Wat berekent dit programma?
```python
num1 = 2
num2 = 4
print(num1 * 3 + num2)
```
Dit programma kan alles berekenen, we hebben geen idee wat het effectief doet. Om dit te verduidelijken zullen we altijd beschrijvende namen gebruiken die het meteen duidelijk maken waar het programma over gaat.

Dit wordt nog verduidelijkt door comments toe te voegen, per blok of per functie zodat elk deel van het programma duidelijk is.

Hieronder hetzelfde programma maar met betere naamgeving en een comment om het doel nog te verduidelijken.
```python
gewonnen = 2
gelijkspel = 4
#voetbal teams verdienen 3 punten voor een winst en 1 voor een gelijkspel.
Print(gewonnen * 3 + gelijkspel)
```

2. Stijlgids

Voor opdrachten en taken moet je de juiste opmaak gebruiken, op de juiste manier werken om het product duidelijk en overzichtelijk te maken. Dit is bij programmeren niet anders.

Verschillende programmeertalen en verschillende bedrijven hebben hun eigen stijlen van programmeren. Deze niet juist of niet volledig volgen maakt de code niet kapot maar vertraagt en bemoeilijkt het werken.

We spreken nu al een aantal stijlregels op. Er zullen er nog bijkomen eens we meer functies leren.

## Spaties en witlijnen

Voor en na een operator typen we altijd een spatie en voor of na een haakje nooit. Stukken code die samenwerken scheiden we van elkaar door een witlijn zoals we paragrafen gebruiken in een tekst.

JUIST:

    hoogte = 10
    oppervlakte = (4 + 7) / 2 * hoogte
    print(“de oppervlakte is “ + str(oppervlakte) + “cm.”)

FOUT:

    Hoogte=10
    Oppervlakte (4+7)/2 * hoogte
    Print ( “de oppervlakte is “ + str (oppervlakte) + “cm.” )

## Lengte van een lijn

Een te lange lijn code maakt de bedoeling onduidelijk. Daarom maken we van een lange lijn code vaak een paar lijnen.

JUIST:

    azijn_ml = (3 * 2) + 5
    koffie_ml = (2 / 3) * 8
    totale_hoeveelheid_zuur = azijn_ml + koffie_ml

FOUT:

    Totale_hoeveelheid_zuur = 3 * 2 + 5 + 2 / 3 * 8

Een te lange string breken we in stukken door de string te onderbreken en een nieuwe te starten.

    Bv: “Hoe gaat het met jou?” = “Hoe gaat ” + “het “ + ”met jou?”

Dit stukje (“ + ”) kun je altijd in een string plakken en de + dan met een enter op de volgende lijn plaatsen.

## Commentaar

Als je commentaar noteert doe dit altijd in volzinnen, zo is het altijd duidelijker wat je bedoelt. Na de # plaats je altijd een spatie voor de leesbaarheid.

FOUT:

    #omtrek

JUIST:

    # Ik wil de omtrek van een vierkant berekenen.

Commentaar moet altijd vertellen waarover de code gaat, niet hoe de code werkt.

FOUT:

    # de omtrek is basis + hoogte

JUIST:

    # Ik wil de omtrek van een rechthoek berekenen.

## Variabelen benoemen

Hierover hebben we het in een vorige les al gehad maar hier wordt nog kort een overzicht gegeven over hoe een goede variabele te kiezen.

We schrijven een variabele altijd zonder hoofdletters en we scheiden verschillende woorden met een liggend streepje. Een variabele is beter te lang en duidelijk dan onduidelijk afgekort. Er moet altijd een naam gekozen worden die zo duidelijk mogelijk zegt waarvoor de variabele gebruikt zal worden.

JUIST:

    titel = “python stijlgids”
    aantal_woorden = 712
    publicatie_jaar = 2024
    auteur = “Swyns”
    kan_document_aanpassen = False
FOUT:

    stijlgids = “python stijlgids”
    x = 712
    publicatiejaar = 2024
    geschreven_door = “Swyns”
    toestemming_aanpassen = False
    
## Stijlregels overzicht

| Stijlregel | Beschrijving |
|------------|--------------|
| Formateren van Code | Code netjes indelen en spaties correct plaatsen rond operatoren. Vermijd willekeurige hoofdletters.|
| Commentaar Toevoegen | Gebruik volzinnen en plaats een spatie na #. Commentaar moet de bedoeling uitleggen, niet de werking. |
| Regels Kort Houden | Breek lange regels code in meerdere lijnen om leesbaarheid te vergroten. |
| Spaties en Witregels | Plaats spaties rond operatoren en geen spatie voor/na haakjes. Gebruik witregels om samenwerkende blokken te scheiden.|
| Beschrijvende Namen | Gebruik duidelijke, beschrijvende namen voor variabelen die aangeven waar de variabele voor gebruikt wordt.|
|Variabelen Benoemen | Gebruik kleine letters met underscores (_) om woorden te scheiden. Vermijd afkortingen als dat onduidelijk is.|