import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from PIL import Image

# Verbinde dich mit der MySQL-Datenbank
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zwiebel55",
    database="face_recognition"
)
cursor = db.cursor()

# Lade die Daten aus der Datenbank
query = "SELECT name, timestamp, image_base64 FROM log"
cursor.execute(query)
rows = cursor.fetchall()
cursor.close()
db.close()

# Erstelle ein DataFrame aus den geladenen Daten
df = pd.DataFrame(rows, columns=['Name', 'Timestamp', 'ImageBase64'])

# Konvertiere die Timestamps zu datetime-Objekten
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Zeige die ersten paar Einträge des DataFrames an
print(df.head())

# Erstelle eine Statistik über die Häufigkeit der erkannten Namen
name_counts = df['Name'].value_counts()

# Zeige die Statistik an
print(name_counts)


# Zeige die Bilder der letzten Erkennungen an
fig, axes = plt.subplots(2, 5, figsize=(15, 60))
for ax, (index, row) in zip(axes.flatten(), df.tail(60).iterrows()):
    image_data = base64.b64decode(row['ImageBase64'])
    image = Image.open(BytesIO(image_data))
    ax.imshow(image)
    ax.set_title(f"{row['Name']}\n{row['Timestamp']}")
    ax.axis('off')

plt.show()
