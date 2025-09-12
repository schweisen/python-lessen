    
from microbit import *
import log

# configuratie
LIGHT_THRESHOLD = 100  # <<< Verander dit naar je 'gemeten' lichtniveau
HYSTERESIS = 8

DARK_THRESHOLD = LIGHT_THRESHOLD - (HYSTERESIS / 2) - HYSTERESIS
LIGHT_ON_THRESHOLD = LIGHT_THRESHOLD - (HYSTERESIS / 2)

ON_IMAGE = Image('99999:99999:99999:99999:99999')
OFF_IMAGE = Image('00000:00000:00900:00000:00000')

# definieer de Variabelen
is_light_on = False
current_event_start_time_ms = 0 # slaat de running_time() op wanneer het licht aan gaat.
total_light_on_duration_ms = 0 # Slaat de totale licht-aan tijd op.

# Opslag van data
# Label de data
# 'EventStart_ms': de running_time() wanneer het licht aanging bij dit evenement.
# 'Duration_ms': hoe lang het licht aan was bij dit specifieke evenement.
log.set_labels('EventStart_ms', 'Duration_ms')

# Hulp functie
def show_number(n):
    # Maak de nummer display hetzelfde als bij MakeCode
    if len(str(n)) == 1:
        display.show(n)
    else:
        display.scroll(n)

# Initialiseren
display.show('L')
sleep(1000) # Geef wat tijd om de microbit op de juiste plaats te plaatsen voor de meting begint.


# meting
while True:
    current_light_level = display.read_light_level()
    current_time_ms = running_time()

    # Controleert of het licht uitgaat.
    if current_light_level < DARK_THRESHOLD:
        if is_light_on:
            # Het licht ging uit, het was hiervoor dus aan.
            event_duration_ms = current_time_ms - current_event_start_time_ms
            total_light_on_duration_ms += event_duration_ms
            
            # sla dit licht-aan evenement op.
            log.add(
                EventStart_ms=current_event_start_time_ms,
                Duration_ms=event_duration_ms
            )
            # Een korte flits om te tonen dat er data opgeslagen is.
            display.show(Image.YES)
            sleep(100)
            display.clear()
            
            is_light_on = False # terug resesetten voor de volgende meting.

    # Controleer of het licht aangaat.
    elif current_light_level >= LIGHT_ON_THRESHOLD:
        if not is_light_on:
            # Het licht ging net aan, een nieuw evenement begint.
            current_event_start_time_ms = current_time_ms
            is_light_on = True # Update status

    # Button B om de totale tijd te tonen.
    if button_b.was_pressed():
        # bereken en toon de totale tijd in minuten.
        minutes_total = total_light_on_duration_ms / 1000
        if is_light_on:
            # Pas live aan als het licht aan is wanneer je op de B button klikt.
            minutes_total += (current_time_ms - current_event_start_time_ms) / 60000
            
        display.clear()
        show_number(round(minutes_total))  # enkel gehele getallen tonen.
        sleep(2000)
        display.clear()

    # Update de display met een ON/OFF status.
    if is_light_on:
        display.show(ON_IMAGE)
    else:
        display.show(OFF_IMAGE)
        
    sleep(500) # korte slaapmodus om verder te kunnen meten maar niet te kort om geen honderden metingen te krijgen.

  
