from PIL import Image
import os



def resize(image):
	(old_width, old_height) = image.size
	aspect_ratio = (1.0*old_height)/(1.0*old_width)
	new_height = aspect_ratio*(500)
	new_size = (500, new_height)
	image = image.thumbnail(new_size)
	#return image


def BlackWhite(image):
	image=image.convert(mode="L")
	return image


# for f in os.listdir('.'):
# 	if f.endswith('.jpg'):
# 		i=Image.open(f)
# 		fn, fext = os.path.splitext(f)
# 		 print fn
# 		print fext 
# 		i.thumbnail(size)
# 		i.save('new.jpg')


''' Step 1: Resize but keep the aspect ratio same because you dont want to squish your image '''
#creating image object
#image1 = Image.open('img.jpg')

if __name__ == '__main__':
	
	filename=raw_input() #input image name

	List=[]
	for f in os.listdir('.'):
		List.append(f)

	if filename in List:
		
		image = Image.open(filename) #.convert('RGB').save('new.jpg') 
		#filename='new.jpg'
		# fn, fext = os.path.splitext(filename)
		# image1=image1.convert(mode='L')
		# image1=image1.rotate(90)
		# image1.save('{}_new.jpg'.format(fn))
		# image1 = Image.open('{}_new.jpg'.format(fn))
		# image1.show()


		#Resize the image
		resize(image)


		#Black&White
		image=BlackWhite(image)

		image.show()
	
	else:
		print (" File not found :( ")


