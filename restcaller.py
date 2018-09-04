# restcaller.py
'''
Custom class to call rest API with authentication

'''
import requests
import json

class RestCaller():


    def __self__(self):
        pass

    #authentication
    def auth(self, url, user, password):
        global access_token, acc_header
        status_code = -1
        if url == None or user == None or password == None :
            return status_code

        payload=  {
        	"username":user,
        	"password":password
        }
        r = requests.post(  url, json=payload)
        status_code = r.status_code
        print('status_code : ' + str(status_code))

        if status_code != 200 :
            return status_code

        # authentication successfull
        access_token = 'JWT ' + r.json()['access_token']
        acc_header = {'Authorization':  access_token}

        return status_code

    #get
    def get(self, url):

        status_code = -1
        print(url)
        if url == None  :
            return status_code

        print(acc_header)
        r = requests.get(  url, headers=acc_header)
        status_code = r.status_code
        print('Getstatus_code : ' + str(status_code))
        if status_code != 200 :
            return status_code

        return status_code

    #responseText
    def post(self, url):

        status_code = -1
        print(url)
        if url == None :
            return status_code



        r = requests.post(  url, headers=acc_header )
        status_code = r.status_code
        print('Post status_code : ' + str(status_code))
        if status_code != 200 :
            return status_code

        return status_code



# end class
#############################################################################

def test_class():
    print('test_class')
    test_caller = RestCaller()

    url = 'http://127.0.0.1:5000/auth'
    status = test_caller.auth(url, "kishore", "1234")
    print (status)



    status = test_caller.post( 'http://127.0.0.1:5000/kpi/Jacky')
    print (status)

    url = 'http://127.0.0.1:5000/kpi/Jacky'

    status = test_caller.get( url)
    print (status)

# end test_class
##############################################################################

test_class()
