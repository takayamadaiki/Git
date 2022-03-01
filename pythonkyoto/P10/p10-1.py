import tkinter as tkinter
import math
import time

class MyFrame(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.size = 200
    self.clock = tk.Canvas(self, width=self.size,height=self.size, background="white")
    self.clock.grid(row=0, column=0)

    self.font_size = int(self.size/15)
    for number in range(1,12+1):
      x = self.size/2 + math.cos(math.radians(number*360/12 - 90))*self.size/2*0.85

      y = self.size/2 + math.sin(math.radians(number*360/12 - 90))*self.size/2*0.85

      self.clock.create_text(x,y,text=str(number),fill="black", font=("",14))