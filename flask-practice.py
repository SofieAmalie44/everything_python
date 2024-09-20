from flask import Flask, request, jsonify
# set up flask server
app = Flask(__name__)


#  to make app accessable 
@app.route("/")

# more complicated route with a path peramiter
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data ={
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extre")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200 # this line makes the return on the api request readable json 


# defines a python function to greate a route
def home():
    return "Home"

# running the flask server
if __name__ == "__name__":
    app.run(debug=True)

# now run the code in the terminal