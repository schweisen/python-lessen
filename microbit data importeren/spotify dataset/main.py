import csv

with open('meeste gestreamde liedjes.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    # We slaan de header (de eerste rij) over
    header = next(reader)
            #tabel-hoofding benoemen
    TRACK_NAME_INDEX = header.index('track_name')
    ARTISTS_INDEX = header.index('artist(s)_name') # Let op: in veel datasets heet deze kolom 'artists_name' of 'artist_name'
    DANCEABILITY_INDEX = header.index('danceability_%') # In veel datasets eindigt dit op _%
    POPULARITY_INDEX = header.index('streams')
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

    for row in reader:
        danceability_score = int(row[DANCEABILITY_INDEX])
        if danceability_score > 90:
            track_name = row[TRACK_NAME_INDEX]
            artists = row[ARTISTS_INDEX]
            print(f"- {track_name} door {artists}")
    
                