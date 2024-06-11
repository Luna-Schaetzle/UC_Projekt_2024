import cv2
import mediapipe as mp
import time

# IP Adresse der ESP32-CAM
ipAdress = '192.168.75.105'
# Streaming Adresse aufbauen
streamAddress = 'http://' + ipAdress + ':81/stream'

# Mediapipe initialisieren
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(streamAddress)

# Initialisieren der Gesichtserkennung
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Lesen des Frames.")
            break
        
        # Konvertiere das Bild von BGR zu RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Gesichtserkennung
        results = face_detection.process(image)
        
        # Konvertiere das Bild zurück zu BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Wenn ein Gesicht erkannt wird
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
                # Speichere das Bild mit Zeitstempel
                timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
                cv2.imwrite(f"images/face_{timestamp}.jpg", frame)
                print(f"Gesicht erkannt und Bild gespeichert: face_{timestamp}.jpg")
        
        cv2.imshow('frame', image)
        
        # ESC Taste zum Abbrechen
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
