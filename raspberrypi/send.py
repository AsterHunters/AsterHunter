import requests
import base64
import json

API_TRANSFER_URL = "http://192.168.1.204:1080/api/transfer.py"

"""
Main function.
"""
def main():
	
	data = dict()
	images = []

	# Account data
	account = dict()
	conf = open("aster.conf", 'r')
	lines = conf.readlines()
	account["username"] = lines[0].split()[1]
	account["password"] = lines[1].split()[1]

	# Coords data
	coords = dict()
	coords["rightAscension"] = ""
	coords["declination"] = ""

	while(len(images) < 3):
		image = dict()
		image["date"] = "asdf"
		image["code64"] = convert_image("butterfly.jpg")
		images.append(image)

	data = dict()
	data["account"] = account
	data["coords"] = coords
	data["images"] = images
	
	response = requests.post(API_TRANSFER_URL, data=json.dumps(data))
	json_data = json.loads(response.text)
	code = json_data['code']
	print code

"""
This function encode in code-64 an image passed from path.
@param path: string, the path of the file to encode.
@return the string in code-64 that represent the image.
"""
def convert_image(path):
	# Open an image and convert in code-64
	with open(path, "rb") as image_file:
		code_64_image = base64.b64encode(image_file.read())
	
	return code_64_image

if __name__ == "__main__":
	main()