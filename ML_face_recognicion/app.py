import cv2
import face_recognition
import pickle
import mysql.connector
from datetime import datetime
import pyttsx3
import base64
from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

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

last_seen_name = None  # Zuletzt erkannter Name

def capture_and_recognize():
    global last_seen_name
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
            if name != "Unbekannt" and name != last_seen_name:
                last_seen_name = name
                message = f"Hallo, {name}!"
                print(message)
                # Text-to-Speech
                engine.say(message)
                engine.runAndWait()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Bild als Base64 kodieren
                _, buffer = cv2.imencode('.jpg', frame)
                image_base64 = base64.b64encode(buffer).decode('utf-8')
                
                cursor.execute("INSERT INTO log (name, timestamp, image_base64) VALUES (%s, %s, %s)", (name, timestamp, image_base64))
                db.commit()

@app.route('/')
def timeline():
    cursor.execute("SELECT name, timestamp, image_base64 FROM log")
    records = cursor.fetchall()

    # Daten für den Zeitstrahl vorbereiten
    data = []
    for row in records:
        name, timestamp, image_base64 = row
        timestamp = pd.to_datetime(timestamp)
        image_src = f"data:image/jpeg;base64,{image_base64}"
        data.append({'Name': name, 'Timestamp': timestamp, 'Image': image_src})

    df = pd.DataFrame(data)

    fig = px.timeline(df, x_start="Timestamp", x_end="Timestamp", y="Name", hover_data=['Image'])
    fig.update_yaxes(categoryorder="total ascending")
    
    timeline_html = fig.to_html(full_html=False)

    return render_template('timeline.html', plot=timeline_html)

if __name__ == '__main__':
    app.run(debug=True)

while True:
    # Erkenne Gesichter und zeige persönliche Nachricht an
    capture_and_recognize()

    # ESC Taste zum Abbrechen
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
