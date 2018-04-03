import io
from google.cloud import vision

vision_client = vision.Client()

file_name = 'input.jpg'

with io.open(file_name,'rb') as image_file:
	image = vision_client.image(content = image_file.read())

labels = image.detect_labels()

for label in labels:
	print (label.description)
	print (label.score)
	print (label.locations)