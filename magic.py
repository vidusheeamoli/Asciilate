from PIL import Image
import os


character_box = ['.',',',':',';','+','*','?','%','S','#','@']


def alter(image):
	(old_width, old_height) = image.size
	aspect_ratio = (1.0*old_height)/(1.0*old_width)
	new_height = aspect_ratio*(100)
	new_size = (100, new_height)
	image = image.thumbnail(new_size)
	#return image


def pigment(image):
	image=image.convert(mode="L")
	return image


def pixel_to_ascii(image):
	pixel_info = list(image.getdata())
	pixels_to_chars = [character_box[pixel_value/25] for pixel_value in pixel_info]
	return "".join(pixels_to_chars)


if __name__ == '__main__':
	filename=raw_input() #input image name
	List=[]
	for f in os.listdir('.'):
		List.append(f)
	if filename in List:
		image = Image.open(filename) #.convert('RGB').save('new.jpg') 
		alter(image)
		image=pigment(image)
		pixels_to_chars = pixel_to_ascii(image)
		len_pixels_to_chars = len(pixels_to_chars)
		image_ascii = [pixels_to_chars[index: index + 100] for index in xrange(0, len_pixels_to_chars, 100)]
		final_ascii_image = "\n".join(image_ascii)
		print final_ascii_image
		file_name , file_extention = os.path.splitext(filename)
		file_object = open('{}.txt'.format(file_name) , "w+")
		file_object.write(final_ascii_image)
		file_object.close()
	else:
		print (" File not found :( ")





