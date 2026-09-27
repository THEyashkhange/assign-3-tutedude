"""1.Create a Flask application with an /api route. When this route is accessed, it should return a JSON list. The data should be stored in a backend file, read from it, and sent as a response."""


from flask import Flask, jsonify, render_template 
import json
import os

app = Flask(__name__)
FILE = os.path.join(os.path.dirname(__file__), 'data1.json')

@app.route('/')
def take_to_api():
    return render_template('index.html')



@app.route('/api')
def read_file():
    if not os.path.exists(FILE):
        return jsonify({"error": "file not found"})
    with open(FILE, 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)