from PIL import Image
import os

character_box = ['.',',',':',';','+','*','?','%','S','#','@']

def resize(image):
	(old_width, old_height) = image.size
	aspect_ratio = (1.0*old_height)/(1.0*old_width)
	new_height = aspect_ratio*(100)
	new_size = (100, new_height)
	image = image.thumbnail(new_size)
	#return image


def black_white(image):
	image=image.convert(mode="L")
	return image


def pixel_to_ascii(image):
	pixel_info = list(image.getdata())
	pixels_to_chars = [character_box[pixel_value/25] for pixel_value in pixel_info]
	return "".join(pixels_to_chars)


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
		image=black_white(image)

		pixels_to_chars = pixel_to_ascii(image)

		len_pixels_to_chars = len(pixels_to_chars)

		image_ascii = [pixels_to_chars[index: index + 100] for index in xrange(0, len_pixels_to_chars, 100)]

		final_ascii_image = "\n".join(image_ascii)

		print final_ascii_image

	
	else:
		print (" File not found :( ")





