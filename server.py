from flask import Flask
app = Flask(__name__)

from website_parser import *

@app.route("/")
def hello():
    return parse_hunter()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
