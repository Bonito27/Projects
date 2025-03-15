import cv2
import os
import numpy as np
import face_recognition
import time

# Storage for faces
FACE_DIR = "C:/Users/Bonit0/Desktop/python_ogreniyorum/face/faces"  #!!!!If you test this code CHANGE THIS LINE!!!!!!

os.makedirs(FACE_DIR, exist_ok=True)

# Start Camera
vid = cv2.VideoCapture(0)

# OpenCV face model 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# List for knowing faces 
known_face_encodings = []
known_face_names = []

def load_known_faces():
    #  loads previously saved faces 
    global known_face_encodings, known_face_names
    known_face_encodings = []
    known_face_names = []

    for file in os.listdir(FACE_DIR):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_path = os.path.join(FACE_DIR, file)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:  # if encoding have
                known_face_encodings.append(encodings[0])
                known_face_names.append(file.replace(".jpg", "").replace(".png", ""))

#loads previously saved faces
load_known_faces()

while True:
    ret, frame = vid.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        # OpenCV convert face to rgb
        rgb_face = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_face, model="hog")

        if face_encodings:  # if deceted face 
            face_encoding = face_encodings[0]  # Take first encoding
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                matched_index = matches.index(True)
                name = known_face_names[matched_index]
            else:
                # Save new face 
                timestamp = int(time.time())  # Uniq name
                filename = f"{FACE_DIR}/face_{timestamp}.jpg"
                save_success = cv2.imwrite(filename, face_img)  #Control for save file

                

                # Save new face in memory
                known_face_encodings.append(face_encoding)
                known_face_names.append(f"face_{timestamp}")

            # Print name on screen
            cv2.rectangle(frame, (x, y), (x + w, y + h), (85, 255, 0), 3)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face ", frame)

    # Press "q" for exit!
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
