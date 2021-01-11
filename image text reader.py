# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:51:13 2021
"""

import cv2
import pytesseract
from pytesseract import Output

#read the image using opencv
img = cv2.imread('x.png')
#using pytesseract to read the text on the image
d = pytesseract.image_to_data(img, output_type=Output.DICT)

#display keys and values of the dict
print(d.keys()
print(d.values())

#extract only the text/words 
l=list(d.get('text'))
print(l)

#processing to display the text using new lines breaks
total=' '.join(l)
total_split=total.split('  ')
str_list = list(filter(None, total_split))
text='\n'.join(str_list)
print(text)

#saving to a txt file
file = open("x.txt", "w")
file.write(text)
file.close()
