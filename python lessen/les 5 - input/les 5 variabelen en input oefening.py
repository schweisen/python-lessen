# taal codes bevatten "nl" voor Nederlands, "es" voor Spaans en "fr" voor Frans.
taal = input("In welke taal wil je de website lezen(nl,es,fr)? ")
# onderwerpen kunnen wiskunde, wetenschappen, economie of menswetenschappen.
onderwerp = input( "Over welk onderwerp wil je lezen (wiskunde, wetenschappen, economie, menswetenschappen)? ")
url = "https://" + taal + ".wikipedia.com/" + onderwerp
print("Ga naar de onderstaande " + onderwerp + " pagina!")
print(url)