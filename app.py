from flask import Flask, jsonify
from datetime import date

#create an instance of the Flask class
app = Flask(__name__)

#define the home route
@app.route('/')
def home():
    return "Welcome to my Flask Web Services!"

#Define the API route
@app.route( '/api', methods=['GET'])
def api():
    data = {"message" : "This is a simple API response"}
    return jsonify(data)


@app.route('/getdate', methods=['GET'])
def getdate():
    data={"message": date.today()}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)