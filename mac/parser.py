import cv2 as cv
import numpy as np
import pytesseract
import pyperclip
from PIL import Image 

#set pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'/Usr/local/bin/tesseract'

class Parser:
    def __init__(self, img):
        self.text = pytesseract.image_to_string(img)
    
    def __str__(self):
        return self.text
    
