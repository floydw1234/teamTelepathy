#!/usr/bin/python


import Tkinter as tk
from PIL import Image, ImageTk
from ttk import Frame, Button, Style
import time

class window():
	def __init__(self, imageFile1, imageFile2, **kwargs):
		
		
		self.root = tk.Tk()
		self.root.title('My Pictures')

		# pick an image file you have.bmp.jpg.gif..png# load the file and covert it to a Tkinter image object
		self.image1 = ImageTk.PhotoImage(Image.open(imageFile1))
		self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))

		# get the image size
		w = self.image1.width()
		h = self.image1.height()

		# position coordinates of root 'upper left corner'
		x = 0
		y = 0
		pad = 3

		# make the root window the size of the image
		self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth()-pad, self.root.winfo_screenheight()-pad))

		self._geom='200x200+0+0'
		self.root.bind('<Escape>',self.toggle_geom)  

		# root has no image argument, so use a label as a panel
		self.panel1 = tk.Label(self.root, image = self.image1)
		self.display = self.image1
		self.panel1.pack(side = tk.TOP, fill = tk.BOTH, expand = tk.YES)
		print "Display image1"
		self.root.after(3000, self.update_image)
		self.root.after(6000, self.update_image)
		self.root.mainloop()

	
	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom	


	def update_image(self):
		print "wtf"
		if self.display == self.image1:
			self.panel1.configure(image = self.image2)
			print "Display image2"
			self.display = self.image2
		else :
			self.panel1.configure(image = self.image1)
			print "Display image1"
			self.display = self.image1
		self.root.after(3000, self.update_image) 
       
