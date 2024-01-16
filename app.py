from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/mess")
def index():
    return {"message":"Hello"}

if __name__ =='__main__':
    app.run(debug=True, port = 9000)

           