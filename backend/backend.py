from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
#CORS(app)
users = { 
    "users_list" :
    [
        {  
            "id" : "xyz567",
            "username" : "teddy",
            "email" : "xyzteddy@calpoly.edu",
            "university" : "Cal Poly"
        },
        {
            "id" : "abc567",
            "username" : "bcdasilv",
            "email" : "bcdasilv@calpoly.edu",
            "university" : "Cal Poly"
        },
        {
            "id" : "yat999",
            "username" : "qwerty",
            "email" : "qwerty@mit.edu",
            "university" : "MIT"
        },
        {
            "id" : "oxz888",
            "username" : "gaby",
            "email" : "gaby33333@cuesta.edu",
            "university" : "Cuesta"
        }, 
        {
            "id" : "zap555",
            "username" : "gaby",
            "email" : "gaby5555@cuesta.edu",
            "university" : "Cuesta"
        } 
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
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
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
    elif request.method == 'DELETE':
      userToDelete = request.get_json()
      users['users_list'].remove(get_user(userToDelete["id"]))
      resp = jsonify(success=True)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
    return users

@app.route('/users/<id>')
def get_user(id):
    if id :
        for user in users["users_list"]:
            if user["id"] == id:
                return user
        return ({})
    return users

@app.route('/users/<university>/<username>')
def get_userUniName(university, username):
    if(university and username):
        matches = {'users_list' : []}
        for user in users["users_list"]:
            if((user["university"] == university) and
                (user["username"] == username)):
                matches['users_list'].append(user)
        return matches
    return users