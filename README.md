### Projektdefinition
Du planst ein System, das folgende Funktionen integriert:

1. **Gesichtserkennung mit einer Kamera über ESP32:** Eine Kamera, verbunden mit einem ESP32-Mikrocontroller, soll Gesichter erkennen können. Wenn ein Gesicht erkannt wird, wird das entsprechende Bild erfasst.

2. **Bildübertragung mittels MQTT an einen Raspberry Pi:** Das erfasste Bild wird vom ESP32 über das MQTT-Protokoll an einen Raspberry Pi gesendet. MQTT wird hier wegen seiner Leichtigkeit und Effizienz in IoT-Anwendungen verwendet.

3. **Interaktion und Speicherung:** Der Raspberry Pi erkennt, dass ein Gesicht im Bild vorhanden ist, begrüßt den Benutzer über ein Mikrofon und speichert das Bild in einer MySQL-Datenbank.

### Geplante Erweiterungen
1. **Anzeige einer Bildkollage auf einem kleinen Bildschirm:** Ein kleiner Bildschirm, verbunden mit dem System, soll eine Kollage aus den gespeicherten Bildern anzeigen.

2. **Transformation in einen virtuellen Avatar:** Ein Live-Bild wird in Echtzeit in einen virtuellen Avatar umgewandelt und auf einem Bildschirm über MediaPipe angezeigt. Dies könnte eine anspruchsvollere Erweiterung sein, da es Echtzeit-Datenverarbeitung und fortgeschrittene Grafikmanipulationen erfordert.

3. **Webserver-Hosting für Datenbankzugriff:** Ein Webserver soll gehostet werden, um den Zugriff auf die Bilder in der MySQL-Datenbank zu ermöglichen. Dies würde es ermöglichen, die gespeicherten Bilder von einem Browser aus zu durchsuchen und zu verwalten.

### Technische Überlegungen
- **Gesichtserkennungssoftware:** Mittels MediaPipe könnte die Gesichtserkennung implementiert werden. Diese Bibliotheken bieten umfangreiche Funktionen zur Bildverarbeitung und Gesichtserkennung.
- **MQTT-Broker:** Wird auf dem Raspberry Pi benötigt, um die Kommunikation zwischen dem ESP32 und dem Raspberry Pi zu ermöglichen.
- **Datenbankspeicherung:** MySQL wird auf dem Raspberry Pi benötigt, um die Bilder und möglicherweise die Benutzerdaten zu speichern.
- **Audioausgabe:** Für die Begrüßung mittels Mikrofon muss eine Audioausgabe eingerichtet werden, möglicherweise mit einer Text-to-Speech-Software. 
- **Bildschirm für Bildanzeige:** Ein kleiner Bildschirm, der an den Raspberry Pi angeschlossen ist, könnte für die Anzeige der Bildkollage verwendet werden.
- **MediaPipe für Avatar-Darstellung:** Für die Umwandlung in einen Avatar und dessen Darstellung kannst du MediaPipe nutzen, eine Bibliothek, die für solche Echtzeitbildverarbeitungs-Aufgaben ausgelegt ist.
- **Webserver für Fernzugriff:** Ein leichtgewichtiger Webserver wie Flask könnte genutzt werden, um den Zugriff auf die Bilder über das Internet zu ermöglichen.


### Technologien
- **ESP32:** Ein Mikrocontroller, der für IoT-Anwendungen geeignet ist. Mit dem speziellen ESP32-CAM-Modul die eine Kamera integriert hat und für Bildverarbeitungsaufgaben geeignet ist.
- **Raspberry Pi:** Ein Einplatinencomputer, der als zentrale Steuereinheit für das System dient. Er kann die Kommunikation mit dem ESP32 über MQTT, die Datenbankverwaltung und die Anzeige von Bildern auf einem Bildschirm übernehmen. 
- **Betreibssystem für Raspberry Pi:** Ein Betriebssystem wie Raspbian, das auf dem Raspberry Pi installiert wird und die notwendigen Softwarepakete für die Funktionalität des Systems enthält.
- **MediaPipe:** Eine Bibliothek für Echtzeitbildverarbeitung, die für die Gesichtserkennung und die Umwandlung in einen Avatar verwendet werden kann.
- **MQTT:** Ein leichtgewichtiges Kommunikationsprotokoll für IoT-Anwendungen, das für die Übertragung von Bildern zwischen dem ESP32 und dem Raspberry Pi verwendet wird.
- **MySQL:** Ein relationales Datenbankmanagementsystem, das für die Speicherung von Bildern und Benutzerdaten verwendet wird.
- **Flask:** Ein Web-Framework für Python, das für die Erstellung eines Webservers zur Verwaltung der Datenbank und der Bilder verwendet werden kann.
- **Text-to-Speech-Software:** Eine Software, die Text in Sprache umwandelt, um die Begrüßung des Benutzers über das Mikrofon zu ermöglichen.
- **Kleiner Bildschirm:** Ein kleiner Bildschirm, der an den Raspberry Pi angeschlossen wird, um die Bildkollage anzuzeigen.
- **Lautsprecher und Mikrofon:** Für die Audioausgabe und -eingabe, die für die Begrüßung des Benutzers und die Interaktion mit dem System benötigt werden.
- **Kamera:** Eine Kamera, die an den ESP32 angeschlossen ist, um Bilder für die Gesichtserkennung zu erfassen.
- **Bildschirm für Avatar-Darstellung:** Ein Bildschirm, der an den Raspberry Pi angeschlossen wird, um den virtuellen Avatar anzuzeigen.

### ESP32-CAM


### Raspberry Pi

#### Betriebssystem



### Bestellliste
- [X] ESP32 Cam Module
- [X] Raspberry Pi 5 mit Gehäuse
- [ ] Eventuell erweiterung: Raspberry Pi 7 Zoll Touchscreen oder andere Bildschirme
- [ ] Eventuell erweiterung: Raspberry Pi Camera Module
- [X] Lautsprecher für Audioausgabe Raspberry Pi
- [X] Raspberry Pi Mikrofon
  
### TODO:
- [X] Alle benötigten Komponenten bestellen
- [ ] ESP32 Kameramodul konfigurieren und Testen
- [ ] Raspberry Pi Betreibssystem installieren und konfigurieren
- [ ] MQTT Broker auf Raspberry Pi installieren
- [ ] MySQL Datenbank auf Raspberry Pi installieren


### Verlauf und Fortschritt
Noch nicht angefangen 

### Teilnehmer
- Maximilian Kili 
- Gabriel Mrkonja 
- Luna Schätzle 
