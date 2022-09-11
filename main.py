import cv2
import csv
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        currDateTime = datetime.now()
        f = open("attendance.csv", "a", newline="")
        row1 = (name, currDateTime.time(), currDateTime.date())
        writer = csv.writer(f)
        writer.writerow(row1)
        f.close()
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
