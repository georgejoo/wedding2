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
    names = request.form.getlist("field_name[]")
    message = request.form['text']
    confirmation = request.form.get('particip')
    if confirmation is None:
        confirmation = request.form.get('nu particip')
    if confirmation == "False":
        flash("Mulțumim pentru răspunsul tău!", category="info")
        report_to_db.add_confirmation(["\n".join(names), message], confirmation)
        return redirect("./")
    elif confirmation == "True":
        flash("Confirmarea a fost trimisă, ne vedem la nuntă!", category="info")
        report_to_db.add_confirmation(["\n".join(names), message], confirmation)
        return redirect("./")
    else:
        return redirect("./")
    # your code


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)