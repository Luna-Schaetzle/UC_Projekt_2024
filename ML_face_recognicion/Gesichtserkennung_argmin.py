import cv2
import face_recognition
import pickle

# Lade das trainierte Modell
with open("face_encodings.pickle", "rb") as f:
    data = pickle.load(f)

# IP Adresse der ESP32-CAM
ipAdress = '192.168.12.84'
# Streaming Adresse aufbauen
streamAddress = 'http://' + ipAdress + ':8080/video'

# Verwende die eingebaute Webcam (index 0)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Fehler beim Lesen des Frames.")
        break

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

    cv2.imshow('Video', frame)

    # ESC Taste zum Abbrechen
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
