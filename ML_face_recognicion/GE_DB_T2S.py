import cv2
import face_recognition
import pickle
import time
import mysql.connector
from datetime import datetime
import pyttsx3

# Lade das trainierte Modell
with open("face_encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Verbinde dich mit der MySQL-Datenbank
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zwiebel55",
    database="face_recognition"
)
cursor = db.cursor()

# Text-to-Speech initialisieren
engine = pyttsx3.init()

# Verwende die eingebaute Webcam (index 0)
cap = cv2.VideoCapture(0)

def capture_and_recognize():
    ret, frame = cap.read()
    if not ret:
        print("Fehler beim Lesen des Frames.")
        return

    # Konvertiere das Bild von BGR zu RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Erkenne Gesichter im Bild
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    recognized_names = []

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(data["encodings"], face_encoding)
        name = "Unbekannt"

        # Berechne die Abstände zwischen dem aktuellen Gesicht und den bekannten Gesichtern
        face_distances = face_recognition.face_distance(data["encodings"], face_encoding)
        best_match_index = face_distances.argmin()

        # Überprüfe, ob der beste Übereinstimmungswert tatsächlich eine Übereinstimmung ist
        if matches[best_match_index]:
            name = data["names"][best_match_index]

        recognized_names.append(name)

        # Zeichne ein Rechteck um das Gesicht und schreibe den Namen
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Erkanntes Bild', frame)
    
    # Persönliche Nachricht anzeigen, als Audio ausgeben und in die Datenbank speichern
    if recognized_names:
        for name in recognized_names:
            if name != "Unbekannt":
                message = f"Hallo, {name}!"
                print(message)
                # Text-to-Speech
                engine.say(message)
                engine.runAndWait()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("INSERT INTO log (name, timestamp) VALUES (%s, %s)", (name, timestamp))
                db.commit()

while True:
    # Warte 10 Sekunden
    time.sleep(10)
    
    # Erkenne Gesichter und zeige persönliche Nachricht an
    capture_and_recognize()

    # ESC Taste zum Abbrechen
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
