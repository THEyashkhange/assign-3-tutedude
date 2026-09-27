from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['form']
collection = db['user']
@app.route('/', methods=['GET', 'POST'])
def home_form():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        if not mail:
            error = "Mail cannot be empty"
        else:
            try:
                collection.insert_one({"name": name,"mail": mail})
                return redirect(url_for('show_success'))
            except Exception as e:
                error = f"Error: {str(e)}"
    return render_template('index.html', error=error)

@app.route('/success',)
def show_success():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)