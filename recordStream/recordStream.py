'''
Beispiel von http://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php
(kleinere Anpassungen durch mich)
'''

import cv2
import time
import os

# IP Adresse der ESP32-CAM
ipAdress = '192.168.75.105'
# Streaming Adresse aufbauen
streamAddress = 'http://' + ipAdress + ':81/stream'

cap = cv2.VideoCapture(streamAddress)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".mp4"
writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

# Maximale Dateigröße in Kilobyte (hier 500 Kb)
max_filesize = 1024 * 500

while True:
    ret, frame = cap.read()
    writer.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1):
        # Auslesen der Dateigröße 
        filesize = os.path.getsize(filename)
        # Wenn die Datei größer ist als das Maximum dann Abbrechen
        if filesize > max_filesize:
            break

    # ESC Taste zum Abbrechen
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()