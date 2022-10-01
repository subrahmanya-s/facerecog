import cv2
import csv
import time
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt
from simple_facerec import SimpleFacerec
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)
d = {}
f = open("attendance.csv", "w", newline="")
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    currDateTime = datetime.now()
    curD = currDateTime.date()
    curT = currDateTime.time()

    store = [("NONE", curD, curT)]
    writer = csv.writer(f)

    for face_loc, name in zip(face_locations, face_names):

        store.append((name, curD, curT))
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    for name in store:
        writer.writerow(name)
    cv2.imshow("Frame", frame)

    time.sleep(1)
    key = cv2.waitKey(1)

cap.release()
f.close()
cv2.destroyAllWindows()
