import pyttsx3

def speak(text):
    # Initialisieren des pyttsx3-Engines
    engine = pyttsx3.init()
    
    # Setzen der Stimmeigenschaften
    rate = engine.getProperty('rate')   # Geschwindigkeit der Sprache
    engine.setProperty('rate', 150)     # Hier kannst du die Geschwindigkeit einstellen (Standardwert ist 200)
    
    volume = engine.getProperty('volume')   # Lautstärke der Sprache
    engine.setProperty('volume', 1.0)       # Hier kannst du die Lautstärke einstellen (0.0 bis 1.0)
    
    # Sprechen des Textes
    engine.say(text)
    
    # Warten, bis das Sprechen abgeschlossen ist
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speak = "Hallo, wie geht es dir heute?"
    speak(text_to_speak)
