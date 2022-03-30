from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """App landing page"""

    return render_template("homepage.html")


@app.route("/get-started")
def getting_started():
    """Starts the decision matrix"""

    return render_template("get-started.html")


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