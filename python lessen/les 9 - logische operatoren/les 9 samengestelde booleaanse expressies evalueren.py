toon = input("is de toon van het comment positief, negatief or neutraal? ")
account_levensduur_in_dagen = int(input("Hoelang bestaat het account al (in dagen)? "))
aantal_woorden_in_comment = int(input("Uit hoeveel woorden bestaat het comment? "))

# negatieve comments komen vaak van accounts die jonger dan een week zijn.
if account_levensduur_in_dagen < 7 or toon == "negatief":
    print("Het comment zal waarschijnlijk niet interessant zijn.")

# positieve comments komen vaak van accounts die ouder dan een maand zijn.
elif account_levensduur_in_dagen > 30 or toon == "positief":
    print("Het comment zal waarschijnlijk interessant zijn.")

# heel korte en heel lange comments zijn vaak niet interessant.
elif aantal_woorden_in_comment < 3 or aantal_woorden_in_comment > 100:
    print("Het comment zal waarschijnlijk niet interessant zijn.")

else:
    print("Het comment zal waarschijnlijk interessant zijn.")