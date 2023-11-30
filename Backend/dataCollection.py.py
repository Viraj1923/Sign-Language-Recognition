import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

#Setting up Camera and Hand Detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

#Initialization and Configuration
offset = 20
imgSize = 300
folder = "Data/Z"
counter = 0

while True:
    #this part of the code is responsible for reading frames from the camera
    #and detecting hands in the frames using the HandDetector object

    #Frame Capture and Hand Detection:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    #Hand Processing and Image Resizing
    if hands:
        # Extracting information about the first detected hand
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        # Displaying Images
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    # Image Saving
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)
