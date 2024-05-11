from flask import flask, render_template
from flask import flask, render_template, request
import my_yelp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    user_submitted_term = request.values.get("term")
    user_submitted_location = request.values.get("location")
    results = my_yelp.search_businesses(user_submitted_term, user_submitted_location)

    return render_template("display_results.html", establishments=results, term=user_submitted_term, location=user_submitted_location)

app.config["TEMPLATE_AUTO_RELOAD"] = True