import cv2
import numpy as np

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load a test image and convert to grayscale
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

# Loop through each face detected and try to recognize it
for (x,y,w,h) in faces:
    # Extract the face ROI (region of interest)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Use the recognition model to predict the ID of the face
    id_, confidence = recognizer.predict(roi_gray)
    
    # If the confidence is high enough, assume the face belongs to the predicted ID
    if confidence < 70:
        # Draw a green rectangle around the face
        color = (0, 255, 0)  # Green
        cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness=2)
        
        # Add the predicted ID as text below the face
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "Person " + str(id_)
        cv2.putText(img, name, (x,y+h+30), font, 1, color, thickness=2)
    else:
        # Draw a red rectangle around the face
        color = (0, 0, 255)  # Red
        cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness=2)
        
        # Add "Unknown" as text below the face
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "Unknown"
        cv2.putText(img, name, (x,y+h+30), font, 1, color, thickness=2)

# Display the image with the detected and recognized faces
cv2.imshow("Face ID", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
