cateraar = input("Wat is de naam van de cateraar? ")
klant = input("Wat is de naam van de klant? ")
contract = ("Dit catering contract wordt afgesloten tussen " 
            + "" + cateraar + "(cateraar) en " + klant + " (klant) " 
            + "(samen partijen) en toont de overeenkomst tussen " 
            + "de partijen aan over de services die de cateraar voor de klant zal uitvoeren " 
            + "op het gevraagde evenement. " + cateraar + " (cateraar) " 
            + "verbindt zich ertoe om de overeengekomen cateringdiensten " 
            + "naar behoren te leveren op de afgesproken datum en locatie," 
            + " zoals beschreven in dit contract. " + klant + " (klant) " 
            + "stemt ermee in om de overeengekomen kosten tijdig te betalen "
            + "en eventuele wijzigingen of annuleringen tijdig door te geven aan "+ cateraar + " (cateraar).")

print("CATERING CONTRACT (" + cateraar + ")")

print("---------------------")

print(contract)