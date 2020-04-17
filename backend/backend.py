from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

users = { 
    "users_list" :
    [
        {  
            "id" : "psych1",
            "name" : "Sean",
            "job" : "Psychic"
        },
        {  
            "id" : "psych2",
            "name" : "Gus",
            "job" : "Pharmaceutical Salesman"
        },
        {  
            "id" : "sbpd1",
            "name" : "Jules",
            "job" : "Detective"
        },
        {  
            "id" : "sbpd2",
            "name" : "Lassy",
            "job" : "Detective"
        },
        {  
            "id" : "sbpd3",
            "name" : "Karen",
            "job" : "Chief"
        }    
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

def random_id():
    return 'unsub' + str(random.randint(0,10000))

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
    elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd["id"] = random_id()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
    return users

@app.route('/users/<id>', methods = ['DELETE'])
def get_user(id):
    if request.method == 'DELETE':
      for user in users["users_list"]:
            if user["id"] == id:
                users["users_list"].remove(user)
      resp = jsonify(success=True)
      resp.status_code = 202 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

    elif id :
        for user in users["users_list"]:
            if user["id"] == id:
                return user
        return ({})
    return users

@app.route('/users/<name>/<job>')
def get_userUniName(name, job):
    if(name and job):
        matches = {'users_list' : []}
        for user in users["users_list"]:
            if((user["name"] == name) and
                (user["job"] == job)):
                matches['users_list'].append(user)
        return matches
    return users