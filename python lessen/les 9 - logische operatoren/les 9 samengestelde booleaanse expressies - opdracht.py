dag = int(input("noteer je geboortedag (1-31): "))
if dag < 1 or dag > 31:
    print("Error. De dag moet tussen 1 en 31 zijn.")

# stap 1
maand = int(input("noteer je geboortemaand (1-12): "))
if maand < 1 or maand > 12:
    print("Error. De maand moet tussen 1 en 12 zijn.")
# stap 2
elif maand in (4,6,9,11):
    if dag > 30:
        print("Error. Deze maand bevat slechts 30 dagen.")

# stap 3
jaar = int(input("noteer je geboortejaar (1900-2025) "))
if jaar < 1900 or jaar > 2025:
    print("Error. Een jaar moet vier cijfers bevatten")

# bonus: februari en het schrikkeljaar
if maand == 2:
    if (jaar % 100) == 0 and (jaar % 400) == 0:
        if dag > 29:
            print("Error. Dit eeuwjaar is een schrikkeljaar, februari bestaat dan maximaal uit 29 dagen.")
    elif (jaar % 100) == 0 and (jaar % 400) != 0:
        if dag > 28:
            print("Error. Dit eeuwjaar is geen schrikkeljaar, februari bestaat dan maximaal uit 28 dagen.") 
    elif (jaar % 4) == 0:
        if dag > 29:
            print("Error. Het is een schrikkeljaar, februari bestaat dan maximaal uit 29 dagen.")
    else:
        if dag > 28:
            print("Error. Februari bevat maximaal 28 dagen als het geen schrikkeljaar is.")