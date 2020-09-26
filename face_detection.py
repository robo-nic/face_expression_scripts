from cv2 import cv2
from time import time_ns

import os


def getUuid(filename):
    extension = filename.split('.')[-1]
    return str(time_ns()) + '.' + extension


# for ref check here - https://realpython.com/face-recognition-with-python

class FaceDetection:

    """
    this method, takes in a input and output directory
    all the images from the input directory are scanned and the detected faces are
    outputted to the output directory
    """

    @staticmethod
    def extractFaces(inputDirectory=None, outputDirectory=None):
        assert(inputDirectory != None)
        assert(outputDirectory != None)

        inputImages = os.listdir(inputDirectory)
        for image in inputImages:
            imagePath = inputDirectory + '/' + image
            FaceDetection.cropToFaces(imagePath, outputDirectory)

    """
    this method crops only the images from all the faces in the passed filepath image file
    if there is no face found, then nothing is saved
    """

    # paths should be absolute to avoid any kind of confusions
    @staticmethod
    def cropToFaces(image, dirPath):
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        img = cv2.imread(image, 0)

        faces = face_cascade.detectMultiScale(
            img, minNeighbors=4, scaleFactor=1.1, minSize=(30, 30))

        # crop faces form the img and save them to the directory
        for (x, y, w, h) in faces:
            # save the images
            cv2.imwrite(dirPath + '/' + getUuid(image), img[y:y+h, x:x+w])
