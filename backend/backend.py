from flask import Flask
from flask import request

app = Flask(__name__)
CORS(app)
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

@app.route('/users')
def get_users():
    search_username = request.args.get('username')
    if search_username :
        subdict = {"users_list" : []}
        for user in users["users_list"]:
            if user["username"] == search_username:
                subdict["users_list"].append(user)
        return subdict
    return users

@app.route('/users/<id>')
def get_user(id):
    if id :
        for user in users["users_list"]:
            if user["id"] == id:
                return user
        return ({})
    return users