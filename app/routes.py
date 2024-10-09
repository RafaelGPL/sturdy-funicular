from flask import Flask             # from the flask module import the Flask class
# OOP -- Object Oriented Paradigm
app = Flask(__name__)               # Create an instance of the Flask class (app is now an object)

@app.get("/")                       # Flask decorator to map routes to view functions
def get_home():                     # Flask view function
    me = {                          # Python dictionary (key-value pairs)
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me                       # When you return a dict in Flask it is converted to JSON!
