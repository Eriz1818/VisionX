import io
import os
from tkinter import filedialog
from shutil import copy
from google.cloud import vision
import tkinter as tk

vision_client = vision.Client()

# open window to select file path
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# copy file to script directory
copy(file_path, '.')

# print ( os.path.basename(file_path) )

# rename file to input.jpg
os.rename(os.path.basename(file_path), 'input.jpg')

file_name = 'input.jpg'

# open file and use vision api on it
with io.open(file_name,'rb') as image_file:
	image = vision_client.image(content = image_file.read())

labels = image.detect_labels()

for label in labels:
	print (label.description)
	print (int(label.score * 100))
	# print (label.locations)