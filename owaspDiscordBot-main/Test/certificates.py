import discord
import firebase_admin
from PIL import ImageFont, ImageDraw, Image  
import cv2  
import numpy as np  
import os
import csv
image = cv2.imread("Certificate.png")
cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im_rgb)  
draw = ImageDraw.Draw(pil_im) 
font = ImageFont.truetype('Lato-Italic.ttf',55)
        # draw = ImageDraw.Draw(img)
name = 'Mahi Maanas Reddy'
year = '100'
x = 625-(len(name)*13.6)
draw.text(xy=(x,350),text=name,fill=(255,255,255),font=font)
draw.text(xy=(770,565),text=year,fill=(255,255,255),font=font)
cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
cv2.imwrite(f'img.png',cv2_im_processed)