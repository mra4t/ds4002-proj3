"""
Created on Sat Nov 12 2022
@author: Ayushi Ambhore 
"""
#run using python3 facedetection.py"

from PIL import Image
import face_recognition
import urllib.request as ur
import cv2
import numpy as np
import pandas as pd
import urllib


# Read in data
movies = pd.read_excel('whitespace.xlsx')

# Keep poster url and movie title
movies = movies[['Poster_Link', 'Series_Title']]

# Loop through every image
facedetection = []


for url in movies['Poster_Link']:
    response = urllib.request.urlopen(url)
    image = face_recognition.load_image_file(response)

    # Find all the faces in the image using the default HOG-based model.
    face_locations = face_recognition.face_locations(image)


    facedetection.append(len(face_locations))

movies['FaceDetection_values'] = facedetection
movies.to_excel('facedetection.xlsx')