import cv2 as cv
import numpy as np
import pandas as pd
import urllib.request as ur
import matplotlib.pyplot as plt

def url_to_image(url): #https://pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
    request = ur.urlopen(url)
    img = np.asarray(bytearray(request.read()), dtype="uint8")
    img = cv.imdecode(img, cv.IMREAD_COLOR)
    return img

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb



# Read in data
movies = pd.read_excel('whitespace.xlsx')

# Keep poster url and movie title
movies = movies[['Poster_Link', 'Series_Title']]

# Loop through every image
color = []
counter = 0
for url in movies['Poster_Link']:
    # Open image from URL
    img = url_to_image(url)

    # img = cv.imread(image)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # dim = (500, 300)
    # # resize image
    # img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    
    img_temp = img.copy()
    unique, counts = np.unique(img_temp.reshape(-1, 3), axis=0, return_counts=True)
    img_temp[:,:,0], img_temp[:,:,1], img_temp[:,:,2] = unique[np.argmax(counts)]
    
    # plt.imshow(img)
    # plt.imshow(img_temp)
    # print(movies['Series_Title'][counter])
    # print(img_temp[0][0][0])
    r = img_temp[0][0][0]
    g = img_temp[0][0][1]
    b = img_temp[0][0][2]

    hex_color = rgb_to_hex((r, g, b))

    color_num = int(hex_color,16)

    # result = (r * 256 * 256) + (g * 256) + b


    # print(color_num)
    # print(result)
    # if counter == 11:
    #     break
    # counter+=1


#     # show_img_compar(img, img_temp)
    color.append(color_num)

movies['Color_value'] = color
movies.to_excel('dominantColor.xlsx')

