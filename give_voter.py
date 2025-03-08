from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.maedirs('data/')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pk1', 'rb') as f:
    FACES = pickle.load(f)

knn=KNeighborsClassifier(n_neighbors=5)

knn.fit(FACES, LABELS)
imgBackground=cv2.imread( )


