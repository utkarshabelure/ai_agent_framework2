from flask import Flask, render_template, request, jsonify
from main import run_task

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/task")
def task():
    return render_template("task.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    user_task = data.get("task", "")

    response = run_task(user_task, mock_mode=True)

    return jsonify(response)   # 🔥 THIS FIXES EVERYTHING

if __name__ == "__main__":
    app.run(debug=True)







