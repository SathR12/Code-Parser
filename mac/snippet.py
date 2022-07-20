from tkinter import *
from parser import *
import pyautogui
import time
import sys
import pyperclip


class Snipping:
    
    def __init__(self, root):
        WIDTH = root.winfo_screenwidth()
        HEIGHT = root.winfo_screenheight()
        self.x, self.y, self.temp_x, self.temp_y = 0, 0, 0, 0
        self.ss = None
        
        self.root = root
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.attributes("-alpha", .3)
        self.root.attributes("-fullscreen", True)
        
  
        self.screen = Canvas(root, cursor = "cross")
        self.screen.pack(fill = BOTH, expand = YES)
     
        #mouse bindings with events
        self.root.bind("<ButtonPress-1>", self.mouse_press)
        self.root.bind("<B1-Motion>", self.mouse_held)
        self.root.bind("<ButtonRelease-1>", self.mouse_release)
        
        #print ss
        return self.ss
        
    def mouse_press(self, event):
        #mouse position on screen to create rect
        self.mouse_x = self.screen.canvasx(event.x)
        self.mouse_y = self.screen.canvasy(event.y)
        
        #create rect
        self.rect = self.screen.create_rectangle(self.x, self.y, 1, 1, outline = "aqua", width = 3, fill = "yellow")
    
    def mouse_held(self, event):
        self.temp_x, self.temp_y = event.x, event.y
       
        #update position
        self.screen.coords(self.rect, self.mouse_x, self.mouse_y, self.temp_x, self.temp_y)
        
    def mouse_release(self, event):
        minimum_x = min(self.mouse_x, self.temp_x)
        minimum_y = min(self.mouse_y, self.temp_y)
        maximum_x = max(self.mouse_x, self.temp_x)
        maximum_y = max(self.mouse_y, self.temp_y)
        
        #print(minimum_x, maximum_x)
        #print(minimum_y, maximum_y)

        self.ss = pyautogui.screenshot(region = (minimum_x, minimum_y, maximum_x - minimum_x,  maximum_y - minimum_y))
        
        self.ss.save("desktop/" + "snippet-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".png")
        PARSER = Parser(self.ss)
        print(PARSER)
        pyperclip.copy(PARSER.__str__())
        self.screen.destroy()
        self.root.destroy()
        sys.exit()
        
        
        

