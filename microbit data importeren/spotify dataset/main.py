import csv

with open('meeste gestreamde liedjes.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    # We slaan de header (de eerste rij) over
    header = next(reader)

    # We lezen en printen de eerste 5 rijen om te testen
    for i in range(5):
        row = next(reader)
        print(row)
#vraag 1
    dualipa_count = 0
    for row in reader:
            # We gaan ervan uit dat de artiest in de TWEEDE kolom staat (index 1).
            # Controleer of de naam 'Dua Lipa' in die kolom voorkomt.
            if 'Dua Lipa' in row[1]:
                # Stap 4: Als dat zo is, tel er eentje bij op.
                dualipa_count += 1
print("aantal keer dat Dua Lipa voorkomt in de hitlijst: "+ str(dualipa_count))
          