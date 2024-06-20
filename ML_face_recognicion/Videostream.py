import cv2

def main():
    # Hier die IP-Adresse und den Port Ihrer Kamera eingeben
    ip_camera_url = 'http://10.10.209.35:8080//video'

    # Videostream von der IP-Kamera öffnen
    cap = cv2.VideoCapture(ip_camera_url)

    if not cap.isOpened():
        print("Fehler beim Öffnen des Videostreams")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Abrufen des Frames")
            break

        # Frame anzeigen
        cv2.imshow('IP Camera Stream', frame)

        # Beenden bei Drücken der 'q' Taste
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Ressourcen freigeben
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
