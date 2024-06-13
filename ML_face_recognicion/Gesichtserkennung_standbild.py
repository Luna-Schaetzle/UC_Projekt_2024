import cv2
import face_recognition
import pickle

# Lade das trainierte Modell
with open("face_encodings.pickle", "rb") as f:
    data = pickle.load(f)

# IP Adresse der ESP32-CAM
#ipAdress = '192.168.12.84'
# Streaming Adresse aufbauen
#streamAddress = 'http://' + ipAdress + ':8080/video'

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

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(data["encodings"], face_encoding)
        name = "Unbekannt"

        # Überprüfe, ob ein bekanntes Gesicht übereinstimmt
        if True in matches:
            first_match_index = matches.index(True)
            name = data["names"][first_match_index]

        # Zeichne ein Rechteck um das Gesicht und schreibe den Namen
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Erkanntes Bild', frame)

# Erste Erkennung durchführen
capture_and_recognize()

while True:
    # ESC Taste zum Abbrechen
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    # Leertaste zum Erfassen eines neuen Bildes
    elif key == 32:
        capture_and_recognize()

cap.release()
cv2.destroyAllWindows()
