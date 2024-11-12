from ultralytics import YOLO
from datetime import datetime
import threading, cv2
from utils import text_to_speech

model = YOLO("models/best.pt")
capture = cv2.VideoCapture(1) # camera index
last_speak = 0
countdown_speak = 7
detect = []

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    results = model(frame, conf = 0.88, verbose = False, imgsz = 640, iou = 0.5)
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            object_name = model.names[class_id]
            if detect.count(object_name) < 3:
                detect.append(object_name)
                continue
            else:
                if detect[0] != object_name:
                    detect = [i for i in detect if i == object_name]

            x1, y1, x2, y2 = box.xyxy[0]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 4)
            cv2.putText(frame, object_name, (int( (x1 + x2) / 2 ) - 200, int(y2)), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

            now = datetime.now().timestamp()
            if now > (last_speak + countdown_speak):
                text = "Uang " + object_name
                threading.Thread(target = text_to_speech, args = (text,)).start()
                last_speak = now

    cv2.imshow("Pendeteksi Nominal Uang Kertas Rupiah", frame)
    if cv2.waitKey(1) == ord('x'):
        break
