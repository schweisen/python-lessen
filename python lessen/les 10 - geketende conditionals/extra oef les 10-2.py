wachtwoord = input("Kies een nieuw wachtwoord: ")

if len(wachtwoord) < 8:
    print("Het wachtwoord moet minstens 8 tekens lang zijn.")
else:
    bevestig_wachtwoord = input("Typ het wachtwoord opnieuw: ")

    if wachtwoord != bevestig_wachtwoord:
        print("Wachtwoorden zijn niet gelijk.")
    else:
        print("Het wachtwoord is veranderd.")
