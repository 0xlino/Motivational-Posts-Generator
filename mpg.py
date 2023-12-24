from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageEnhance
import textwrap
import os
import random

# This was made for good do not just spam the internet with garage, that's bad. 

def get_random_quote():
	"""
	returns a random quote from the quotes file
	@return: a random quote
	"""
	quotes = get_quotes_from_file("in/quotes.txt")
	return quotes[random.randint(0, len(quotes) - 1)]

def get_quotes_from_file(file):
	"""
	reads a file and returns a list of quotes
	@param file: the file to read
	@return: a list of quotes
	"""
	with open(file) as f:
		content = f.readlines()
	return [x.strip() for x in content]

def is_it_a_image(path):
	"""
	checks if a file is an image
	@param path: the path to the file
	@return: True if the file is an image, False otherwise
	"""
	ext = path[-4:]
	if (ext == ".jpg") or (ext == ".png") or (ext == "jpeg"):
		return True
	return False

def get_image_paths(files):
	"""
	returns a list of image paths from a list of files
	@param files: a list of files
	@return: a list of image paths
	"""
	img_paths = []
	for file in files:
		if is_it_a_image(file):
			img_paths.append(file)
	return img_paths

def place_trademark_inside_image(im, trademark, font):
	"""
	places the trademark logo inside the image
	@param im: the image to place the logo on
	@param trademark: the trademark text
	@param font: the font to use for the trademark text
	@return: the image with the trademark logo placed on it
	"""
	draw = ImageDraw.Draw(im)
	bbox =  im.getbbox()
	W = bbox[2]
	H = bbox[3]
	text_width, text_height = draw.textsize(trademark, font=font)
	x = (W - text_width) / 2
	y = H - text_height - 10
	draw.text((x, y), trademark, font=font)
	return im

def apply_tint_to_image(im, tint_color):
	"""
	applies a tint to an image
	@param im: the image to apply the tint to
	@param tint_color: the tint color
	@return: the tinted image
	"""
	tinted_im = ImageChops.multiply(im, Image.new('RGB', im.size, tint_color))
	tinted_im = ImageEnhance.Brightness(im).enhance(.6)
	return tinted_im

def place_logo_on_image(im, logo, trademark, font):
	"""
	places the logo on the image
	@param im: the image to place the logo on
	@param logo: the logo image
	@param trademark: the trademark text
	@param font: the font to use for the trademark text
	@return: the image with the logo placed on it
	"""
	bkg_width = 1080
	bkg_height = 1080
	logo_width, logo_height = logo.size
	draw = ImageDraw.Draw(im)
	text_width, text_height = draw.textsize(trademark, font=font)
	spacing = 2
	x_position = int((bkg_width - logo_width) / 2)
	y_position = bkg_height - logo_height - text_height
	im.paste(logo, (x_position, y_position), logo)
	return im

def place_qoute_at_the_top_of_image(im, quote, font):
	"""
	places the quote on the image
	@param im: the image to place the quote on
	@param quote: the quote text
	@param font: the font to use for the quote text
	"""
	draw = ImageDraw.Draw(im)
	bbox =  im.getbbox()
	W = bbox[2]
	H = bbox[3]
	lines = textwrap.wrap(quote, width=24)
	n_lines = len(lines)
	pad = -10
	current_h = 0
	for line in lines:
		w, h = draw.textsize(line, font=font)
		draw.text(((W - w) / 2, current_h), line, font=font)
		current_h += h + pad
	return im

def place_quote_in_center(im, quote, font):
	"""
	places the quote in the center of the image
	@param im: the image to place the quote on
	@param quote: the quote text
	@param font: the font to use for the quote text
	@return: the image with the quote placed on it
	"""
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(quote, font=font)
	bbox =  im.getbbox()
	W = bbox[2]
	H = bbox[3]
	lines = textwrap.wrap(quote, width=24)
	n_lines = len(lines)
	pad = -10
	current_h = H/2 - (n_lines*h/2)
	for line in lines:
		w, h = draw.textsize(line, font=font)
		draw.text(((W - w) / 2, current_h), line, font=font)
		current_h += h + pad
	return im

def build_final_image(im_path, quote, im_count = '', logoify = True, trademark = '@0xlino'):
	"""
	builds the final image
	@param im_path: the path to the image
	@param quote: the quote text
	@param im_count: the number of the image
	@param logoify: True if the logo should be added, False otherwise
	@return: the final image
	"""
	# qoute is like text - author
	qouteFull = quote
	qouteAuthor = qouteFull.split('-')[1]
	quoteText = qouteFull.split('-')[0]

	# make qouteAuthor like Abraham Lincoln into abraham_lincoln
	qouteAuthorSlug = qouteAuthor.replace(' ', '_').lower()

	W = H = 1080
	im = Image.open(im_path).resize((W,H))
	im = apply_tint_to_image(im, (200,200,200))
	cap_font = ImageFont.truetype("./in/fonts/BebasNeue.otf",115)
	qoute_text_font = ImageFont.truetype("./in/fonts/BebasNeue.otf", 100)
	# im = place_qoute_at_the_top_of_image(im, qouteAuthor, cap_font)
	im = place_quote_in_center(im, quoteText, qoute_text_font)
	if (logoify):
		trademark = qouteAuthor
		tm_font = ImageFont.truetype("./in/fonts/tommy.otf",52)
		im = place_trademark_inside_image(im, trademark, tm_font)
		logo = Image.open("./in/author_images/" + qouteAuthorSlug + ".png")
		# resize the logo to 114x114
		logo = logo.resize((114,114))
		im = place_logo_on_image(im, logo, trademark, tm_font)
	im.save('out/' + str(im_count) + "_" + str(quote[0:10]) + '.png')
	print ("Output image saved as: " + 'out/' + str(im_count) + "_" + str(quote[0:10]) + '.png')

def main():
	"""
	Main function
	"""

	# get the paths to the images
	dir_paths = os.listdir("in/raw")
	im_paths = get_image_paths(dir_paths)

	# get the quotes
	quotes = get_quotes_from_file("in/quotes.txt")

	# ask the user if they want to generate all combinations
	combos = (input("Generate all combinations? (y/n): ") == 'y')

	# ask the user if they want to include the trademark/logo
	logoify = (input("Include trademark/logo? (y/n): ") == 'y')

	# if (logoify):
	# 	# trademark = "@0xlino"
	# 	trademark = input("Enter trademark: ")

	# if the user wants to generate all combinations then generate all combinations
	if combos:
		im_count = 0
		for im_path in im_paths:
			for quote in quotes:
				print ("Overlaying " + str(im_path) + "...")
				build_final_image('in/raw/' + im_path, quote, im_count, logoify, trademark = '@0xlino')
			im_count = im_count + 1
	else:	
		for i, im_path in enumerate(im_paths):
			print ("Overlaying " + str(im_path) + "...")
			build_final_image('in/raw/' + im_path, quotes[i], '', logoify, trademark = '@0xlino')

main()
