from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """App landing page"""

    return render_template("homepage.html")







if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")