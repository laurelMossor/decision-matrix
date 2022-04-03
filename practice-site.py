from flask import Flask, request, render_template
import json
import os
import requests



app = Flask(__name__)

NEWS_API_KEY = os.environ['NEWS_API_KEY']


@app.route("/")
def home():
    """App landing page"""

    return render_template("homepage.html")

@app.route("/news-test-page")
def test_page():
    """Testing APIs"""

    url = "https://newsapi.org/v2/top-headlines"
    payload = {
        "apikey": NEWS_API_KEY, 
        "country": "us",
        "pageSize": "5",
    }

    res = requests.get(url, params=payload)
    data = res.json()
    articles = data["articles"]


    return render_template("news-test-page.html", 
    data=data, 
    articles=articles)


@app.route("/get-started")
def getting_started():
    """Starts the decision matrix"""

    current_user = request.args.get("current-user")
    user_decision = request.args.get("user-decision")
    populated_values = [request.args.get("current-user"), request.args.get("user-decision")]

    return render_template("get-started.html", name=current_user, 
        decision=user_decision, values=populated_values)


@app.route("/identify-criteria")
def identifying_criteria():
    """Walks the user through picking decision criteria"""

    current_user = request.args.get("current-user")
    user_decision = request.args.get("user-decision")

    return render_template("identify-criteria.html", 
        name=current_user, 
        decision=user_decision)





if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")