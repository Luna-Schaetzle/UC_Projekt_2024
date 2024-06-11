import cv2
import mediapipe as mp
import time
import os

# Mediapipe initialisieren
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Verwende die eingebaute Webcam (index 0)
cap = cv2.VideoCapture(0)

# Verzeichnis, um Bilder zu speichern
save_dir = "collected_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

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
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                (x, y, w, h) = (int(bboxC.xmin * iw), int(bboxC.ymin * ih),
                                int(bboxC.width * iw), int(bboxC.height * ih))
                
                # Überprüfen, ob das gesamte Gesicht im Bild ist
                if x > 0 and y > 0 and (x + w) < iw and (y + h) < ih:
                    mp_drawing.draw_detection(image, detection)
                    # Speichere das Bild mit Zeitstempel
                    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
                    person_name = "Luna"  # Hier den Namen der Person eingeben
                    person_dir = os.path.join(save_dir, person_name)
                    if not os.path.exists(person_dir):
                        os.makedirs(person_dir)
                    cv2.imwrite(os.path.join(person_dir, f"{timestamp}.jpg"), frame)
                    print(f"Gesicht erkannt und Bild gespeichert: {person_dir}/{timestamp}.jpg")
        
        cv2.imshow('frame', image)
        
        # ESC Taste zum Abbrechen
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
