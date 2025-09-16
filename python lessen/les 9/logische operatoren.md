# Samengestelde booleaanse operatoren

Wat als er meerdere voorwaarden voldaan moeten zijn voordat iets “true” mag zijn?

    Bv: een leerling mag pas binnen in de jongenskleedkamer als deze én in de juiste klas zit én het juiste geslacht heeft.

Om deze samengestelde vraag te kunnen programmeren gebruiken we een samengestelde booleaanse uitdrukking.

|Operator|Operatie|Voorbeeld|Vraagt?|
|-:|:-:|:-:|-|
|Not|Negatie|Niet x|Is x niet True?|
|And|Verbinding|x en y|Zijn x en y allebei True|
|Or|Ontkoppeling|x of y|Is x of y True?|

Om Booleaanse expressies te combineren gebruiken we dus logische operatoren ‘and’ en ‘or’.

    Bv: zoals hierboven, mag een leerling de jongenskleedkamer binnen?
    Klas == “4BW” and geslacht == “jongen”

De logische operator ‘not’ neemt het omgekeerde van een booleaanse expressie.

    Bv: not (Klas == “4BW” and geslacht == “jongen”)
    Dit vertelt dus of een leerling niet in 4BW zit én geen jongen is.

# Expressies evalueren

Zoals we weten is de output van een booleaanse expressie altijd True of False. Bij een eenvoudige expressie is dit duidelijk maar met ‘and’ en ‘or’ wordt dit ingewikkelder. De logische operatoren komen altijd laatst in de volgorde van bewerkingen.

    Bv: klas == “4BW” and geslacht == “jongen”

We zeggen dat klas = 4BW en geslacht = meisje dan wordt de booleaanse expressie ingevuld als volgt:

    => “4BW” == “4BW” and geslacht == “jongen”
    => True and “meisje” == “jongen”
    => True and False
    => False

# Waarheidstabellen

Een waarheidstabel toont ons alle mogelijke resultaten. Dit geeft een overzicht van alles wat er uit de booleaanse expressie kan komen.

Bv: bij ons voorbeeld

|klas == |geslacht == |Klas == and geslacht ==|
|:-:|:-:|-|
|True|True|True|
|True|False|False|
|False|True|False|
|False|False|False|

Bv: je gsm is vergrendeld en je kunt hem openen met de pincode of met je vingerafdruk.

=> pincode == 12345 or vingerafdruk == “herkent”

|pincode ==|vingerafdruk ==|pincode == or vingerafdruk ==|
|:-:|:-:|-|
|True|True|True|
|True|False|True|
|False|True|True|
|False|False|False|