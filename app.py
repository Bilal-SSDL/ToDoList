from flask import Flask

app_inst = Flask(__name__)

@app_inst.route("/")
def hello():
    return "First flask app"

if __name__ == "__main__":
    app_inst.run()