#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
# Import modules for stdin and JSON
import sys, json
# Impoert modules for open new subprocess
import subprocess

"""
Main function.
"""
def main():
	# Get JSON
	data = sys.stdin.read()
	data_json = json.loads(data)

	# Get value JSON
	username = data_json['username']
	password = data_json['password']
	
	# Send response
	send_response(check_login(username, password))

"""
This function check if a user with username or password is registred in the database.
@param username: string, the username of the user.
@param password: string, the password of the user.
@return boolean, True if the user is present in the dabase, False otherwise.
"""
def check_login(username, password):
	proc = subprocess.check_output(["php", "/var/www/AsterHunter/AsterHunter/html/index.php", "user", "validate", username, password])
	if (int(str(proc)) > 0):
		return True
	else:
		return False

"""
This function get user id.
@param username: string, the username of the user.
@param password: string, the password of the user.
@return int, id.
"""
def get_login(username, password):
	proc = subprocess.check_output(["php", "/var/www/AsterHunter/AsterHunter/html/index.php", "user", "validate", username, password])
	return int(str(proc))

"""
This function send a response to the client.
@param is_positive: boolean, true if it is positive, false otherwise.
"""
def send_response(is_positive):
	
	response = dict()
	
	if is_positive:
		# Make response	
		response["code"] = 0
		response["data"] = "Your login data are valid!"
	else:
		# Make response	
		response["code"] = 1
		response["data"] = "Invalid username or password!"
 	
	# Send response
	print "Content-type:application/json\r\n\r\n"
	print json.dumps(response)

if __name__ == "__main__":
	# Enable debug
	cgitb.enable()

	main()