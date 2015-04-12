#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
# Import modules for stdin and JSON
import sys, json
# Import login
from login import check_login, send_response, get_login
# Import session
#from DarkAster.session import Hunter

"""
Main function.
"""
def main():
	# Get JSON
	data = sys.stdin.read()
	data_json = json.loads(data)

	# Get value JSON
	account = data_json['account']
	username = account['username']
	password = account['password']

	# Check login. If it is all right continue reading JSON
	ida = get_login(username, password)
	if (ida > 0):

		# coords = data_json['coords']

		# images = []
		# dates = []

		# images_dict = data_json['images']
		# for image_dict in images_dict:
		# 	image = image_dict['code64']
		# 	images.append(image)
		# 	date = image_dict['date']
		# 	dates.append(date)
		
		# 	# Decode and save image
		# 	save_image(image, date)

		#hunter = Hunter(ida, images, datas, coords)

		# Send response
		send_response(True)
	else:
		# Send response
		send_response(False)

"""
This function decode and save an image from a base-64 string.
@param image: string, the image in base-64.
@param name: string, the name of the image.
"""
def save_image(image, name):
	# Open and decode image
	image_file = open("../temp/" + name + ".fit", "wb")
	image_file.write(image.decode('base64'))
	image_file.close()

if __name__ == "__main__":
	# Enable debug
	cgitb.enable()

	main()
