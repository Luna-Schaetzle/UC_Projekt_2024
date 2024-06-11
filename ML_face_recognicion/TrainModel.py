import os
import face_recognition
import pickle

# Verzeichnis mit gesammelten Bildern
data_dir = "collected_images"

known_encodings = []
known_names = []

# Durchsuche die Bilder und speichere die Gesichtsembeddings und Namen
for person_name in os.listdir(data_dir):
    person_dir = os.path.join(data_dir, person_name)
    if os.path.isdir(person_dir):
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:
                known_encodings.append(face_encodings[0])
                known_names.append(person_name)

# Speichere die Gesichtsembeddings und Namen
data = {"encodings": known_encodings, "names": known_names}
with open("face_encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("Modell erfolgreich trainiert und gespeichert.")
