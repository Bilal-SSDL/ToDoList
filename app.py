from flask import Flask, render_template

app_inst = Flask(__name__)

@app_inst.route("/")
def home():
    #return "To-Do List Home Page"
    return render_template('home.html')

@app_inst.route("/add")
def add_task():
    return render_template("add_task.html")

@app_inst.route("/update")
def update_task():
    return render_template('update_task.html')

@app_inst.route("/delete")
def delete_task():
    return render_template('delete_task.html')

if __name__ == "__main__":
    app_inst.run(debug=True)