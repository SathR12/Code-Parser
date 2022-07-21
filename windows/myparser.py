import pytesseract

#set pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class myParser:
    def __init__(self, img):
        self.text = pytesseract.image_to_string(img)
    
    def __str__(self):
        return self.text
    
    

        
        
    
    
        
        
        
        
        
    
