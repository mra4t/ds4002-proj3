"""
Created on Thu Nov 10 11:30:38 2022

@author: Maddie
"""
#run using python3 whitespace.py"

import cv2
import numpy as np
import pandas as pd
import urllib.request as ur

def url_to_image(url): #https://pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
    request = ur.urlopen(url)
    img = np.asarray(bytearray(request.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img

# Read in data
movies = pd.read_excel('/Users/Maddie/OneDrive/Desktop/4YEAR/DS4002/Project3/ds4002-proj3/DATA/imdb_top_1000.xlsx')

# Remove rows where gross income is an NA value
movies = movies.dropna(axis=0, how="any", subset="Gross")

# Keep poster url and movie title
movies = movies[['Poster_Link', 'Series_Title']]

# Loop through every image
whitespace = []

for url in movies['Poster_Link']:
    # Open image from URL
    image = url_to_image(url)

    # Compute number of white pixels
    num_white = np.sum(image==255)
    
    #Compute frequency of white pixels (relative to total number of pixels)
    total = image.size
    whitespace_rate = num_white / total
    
    # Add whitespace_rate to whitespace array
    whitespace.append(whitespace_rate) #whitespace percentage / rate

movies['Whitespace_Rate'] = whitespace
movies.to_excel('/Users/Maddie/OneDrive/Desktop/4YEAR/DS4002/Project3/ds4002-proj3/DATA/whitespace.xlsx')
