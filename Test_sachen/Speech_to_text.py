import speech_recognition as sr
import keyboard

def speech_to_text():
    # Initialisieren des Recognizers
    recognizer = sr.Recognizer()

    # Verwenden des Mikrofons als Eingabequelle
    with sr.Microphone() as source:
        print("Sprechen Sie etwas... Drücken Sie die Leertaste, um die Aufnahme zu beenden.")
        
        # Hintergrundgeräusche anpassen und Audio aufnehmen
        recognizer.adjust_for_ambient_noise(source)

        # Warte auf die Leertaste, um die Aufnahme zu beenden
        while not keyboard.is_pressed('space'):
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
            try:
                # Sprachaufnahme in Text umwandeln
                text = recognizer.recognize_google(audio, language="de-DE")
                print("Sie haben gesagt: " + text)
            except sr.UnknownValueError:
                print("Google Speech Recognition konnte das Audio nicht verstehen")
            except sr.RequestError as e:
                print("Konnte keine Ergebnisse von Google Speech Recognition Service anfordern; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
