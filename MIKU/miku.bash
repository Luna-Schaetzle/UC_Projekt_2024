#!/bin/bash

# Starte JACK
jack_control start

# Setze JACK Parameter
jack_control ds alsa
jack_control dps rate 44100
jack_control dps nperiods 3
jack_control dps period 256

# Starte qjackctl (GUI für JACK)
qjackctl &

# Warte einige Sekunden, bis JACK gestartet ist
sleep 5

# Starte Carla
carla &

# Warte einige Sekunden, bis Carla gestartet ist
sleep 5

# Automatische Verbindungen herstellen (wenn möglich)
# Hier wird ein Beispiel für die Verbindung von Mikrofon und Lautsprecher gezeigt
jack_connect system:capture_1 carla-rack:in1
jack_connect carla-rack:out1 system:playback_1
jack_connect carla-rack:out2 system:playback_2

echo "Voice changer läuft. Konfiguriere den Vocoder in Carla. Drücke Strg+C zum Beenden."

# Warte auf Strg+C zum Beenden
trap "jack_control stop; killall qjackctl carla" SIGINT
wait

