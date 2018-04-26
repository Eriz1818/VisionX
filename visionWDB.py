import os , io
from google.cloud import vision
import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="meow",         # your username
                     passwd="meow",  # your password
                     db="visionXpy")

cursor = db.cursor()

### QUERY DATA
# query = ("""SELECT img_name FROM images""")
# cursor.execute(query)
#
# for (img_name) in cursor:
#   print("image name is {}".format(img_name))
# cursor.close()
# db.close()


### INSERT
# add_image = ("""INSERT INTO images (img_name) VALUES (%s)""")
# for file in os.listdir('./timg'):
#     if not file.startswith('.'):
#         # print(file)
#         image_data = (file,)
#         cursor.execute(add_image, image_data)
# db.commit()
# cursor.close()
# db.close()

# vision_client = vision.Client()
#
# photo_categories = dict()
# for file in os.listdir('./timg'):
#     if not file.startswith('.'):
#         # print(file)
#         with io.open('./timg/'+file,'rb') as image_file:
#             image = vision_client.image( content = image_file.read() )
#             labels = image.detect_labels()
#             for label in labels:
#                 if ( int(label.score * 100) > 80 ):
#                     # print( label.description , " score ", int(label.score * 100) )
#                     if label.description not in photo_categories:
#                         photo_categories[label.description] = []
#                         photo_categories.setdefault(label.description, []).append(file)
#                     else:
#                         photo_categories.setdefault(label.description, []).append(file)
#                     # process:  keys will be categories and values will be appended to the keys
# print(photo_categories)

### adding tags to table
# add_tags = ("""INSERT INTO tags (tag_name) VALUES (%s)""")
# for key in photo_categories.keys():
#     tag_data = (key,)
#     cursor.execute(add_tags, tag_data)
# db.commit()

photo_categories = {'wave': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'water': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'sea': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'ocean': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'wind wave': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water6.jpg'], 'body of water': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'sky': ['Water1.jpg', 'Water2.jpg', 'Water5.jpg', 'Water6.jpg'], 'coastal and oceanic landforms': ['Water2.jpg'], 'shore': ['Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'horizon': ['Water2.jpg', 'Water5.jpg', 'Water6.jpg'], 'sunset': ['Water5.jpg'], 'sunrise': ['Water5.jpg'], 'coast': ['Water6.jpg']}

### adding mapping to image_tags
image_tag_query = (""" INSERT INTO image_tags (tag_name, img_name) VALUES (%s, %s) """)

for key in photo_categories.keys():
    for item in photo_categories[key]:
        print (key," ",item)
        cursor.execute(image_tag_query, (key, item))

db.commit()
cursor.close()
db.close()
