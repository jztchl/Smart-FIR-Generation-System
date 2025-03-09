import cv2
from ultralytics import YOLO
import easyocr
import face_recognition
import os
model = YOLO("yolov8n.pt") 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_known_faces(known_faces_folder):

    known_faces = {"names": [], "encodings": []}

    for filename in os.listdir(known_faces_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(known_faces_folder, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_faces["encodings"].append(encodings[0])  
                known_faces["names"].append(os.path.splitext(filename)[0]) 

    return known_faces

def extract_text(image_path):
    reader = easyocr.Reader(['en'])  
    text = reader.readtext(image_path, detail=0)  
    if not text or text == "[]" or text == []:  
        text = "No textual evidence found."
    elif isinstance(text, list):  
        text = " ".join(map(str, text))  
    return text


def detect_objects(image_path):
    results = model(image_path)
    detected = [model.names[int(box.cls)] for box in results[0].boxes]
    return list(set(detected))


def detect_faces(image_name):
    known_faces = load_known_faces("known_faces")
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_encodings = face_recognition.face_encodings(rgb_image)

    detected_faces = []

    for i, (x, y, w, h) in enumerate(faces):
        name = "Unknown"

        if known_faces["encodings"] and i < len(face_encodings):
            matches = face_recognition.compare_faces(known_faces["encodings"], face_encodings[i])
            
            if True in matches:
                match_index = matches.index(True)
                name = known_faces["names"][match_index]

        detected_faces.append({"x": x, "y": y, "w": w, "h": h, "name": name})
        print (detected_faces)
    return detected_faces