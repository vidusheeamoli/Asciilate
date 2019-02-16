from PIL import Image
import os

#creating image object
#image1 = Image.open('img.jpg')

''' Step 1: Resize but keep the aspect ratio same because you dont want to squish your image '''

size= (5000,50)

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i=Image.open(f)
		fn, fext = os.path.splitext(f)
		''' print fn
		print fext '''
		i.thumbnail(size)
		i.save('new.jpg')
 