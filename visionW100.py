import os , io
from google.cloud import vision

vision_client = vision.Client()

photo_categories = dict()
for file in os.listdir('./timg'):
    if not file.startswith('.'):
        # print(file)
        with io.open('./timg/'+file,'rb') as image_file:
            image = vision_client.image( content = image_file.read() )
            labels = image.detect_labels()
            for label in labels:
                if ( int(label.score * 100) > 80 ):
                    print( label.description , " score ", int(label.score * 100) )
                    if label.description not in photo_categories:
                        photo_categories[label.description] = []
                        photo_categories.setdefault(label.description, []).append(file)
                    else:
                        photo_categories.setdefault(label.description, []).append(file)
                    # process:  keys will be categories and values will be appended to the keys
print(photo_categories)