# my-lair-a > app.py

from flask import Flask, render_template, request, flash, redirect
import report_to_db

app = Flask(__name__, static_folder="./static")
app.secret_key = b'amplecatingermania'
# Creating a route to a template is done by:
@app.route('/')
def index():
    return render_template('./index.html')

# Returning an API response can be done like:
@app.route('/response')
def response():
    return {"Message": "Success"}


@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['name']
    number_of_people = request.form['number_of_people']
    print(name, number_of_people)
    flash("Confirmarea a fost trimisa!", category="info")
    report_to_db.add_confirmation([name, number_of_people])
    #return render_template("index.html")
    return redirect("./")
    # your code

if __name__ == '__main__':
    app.run()