import requests
import json



URL = "http://127.0.0.1:8000/students/"


def post():
    data={
    'name':"ckuldeep",
    'rollNo':1222,
    'address':"dsfdsf"}
    json_data = json.dumps(data)
    response = requests.post(url = URL, data=json_data)
    print(response.json())

def get():
    data={
        'id':2
    }
    json_data = json.dumps(data)
    response = requests.get(url=URL,data=json_data)
    print(response.json())

def put():
    data={
        'id':3,
        'name':'updated'
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL,data=json_data)
    print(response.json())

def delete():
    data={'id':2}
    json_data = json.dumps(data)
    response = requests.delete(URL,data=json_data)
    print(response.json())



# delete()


post()
# get()
# put()