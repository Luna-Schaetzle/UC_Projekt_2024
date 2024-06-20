import mysql.connector
import matplotlib.pyplot as plt
import base64
from PIL import Image
from io import BytesIO
import datetime

# Verbinde dich mit der MySQL-Datenbank
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zwiebel55",
    database="face_recognition"
)
cursor = db.cursor()

# Führe eine SQL-Abfrage aus, um die Daten abzurufen
cursor.execute("SELECT name, timestamp, image_base64 FROM log ORDER BY timestamp DESC")
rows = cursor.fetchall()

# Schließe die Verbindung zur Datenbank
cursor.close()
db.close()

# Daten anzeigen
fig, axes = plt.subplots(len(rows), 1, figsize=(10, len(rows) * 3))

for i, (name, timestamp, image_base64) in enumerate(rows):
    # Dekodiere das Base64-kodierte Bild
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    
    # Erstelle einen Titel mit Name und Timestamp
    title = f"Name: {name}\nTimestamp: {timestamp}"
    
    # Zeige das Bild und den Titel an
    if len(rows) > 1:
        axes[i].imshow(image)
        axes[i].set_title(title)
        axes[i].axis('off')
    else:
        axes.imshow(image)
        axes.set_title(title)
        axes.axis('off')

plt.tight_layout()
plt.show()
