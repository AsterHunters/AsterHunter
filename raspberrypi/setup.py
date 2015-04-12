import requests
import json

API_LOGIN_URL = "http://192.168.1.204:1080/api/login.py"

"""
Main function.
"""
def main():
     login()
"""
This function make the login and save username and password into config file.
"""
def login():
     user = str(raw_input('Username: '))
     pswrd = str(raw_input('Password: '))

     data = dict()
     data['username'] = user
     data['password'] = pswrd

     response = requests.post(API_LOGIN_URL, data=json.dumps(data))
     json_data = json.loads(response.text)

     if json_data['code'] == 1:
          print json_data['data']
          return main()

     conf = open("aster.conf", 'w')
     conf.write('Username ' + user + "\n" +'Password ' + pswrd + "\n")

     print json_data['data']

if __name__ == '__main__':
     main()
