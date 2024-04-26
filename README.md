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

### Bestellliste
- [ ] ESP32 Cam Module
- [ ] Raspberry Pi 5 mit Gehäuse
- [ ] Eventuell erweiterung: Raspberry Pi 7 Zoll Touchscreen oder andere Bildschirme
- [ ] Eventuell erweiterung: Raspberry Pi Camera Module
- [ ] Lautsprecher für Audioausgabe Raspberry Pi
  
### TODO:
- [ ] Alle benötigten Komponenten bestellen


### Verlauf und Fortschritt
Noch nicht angefangen 