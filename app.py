from flask import Flask, render_template, request, jsonify
from detector import analyze_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_message():
    data = request.get_json()
    text = data.get("text", "")

    result = analyze_text(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
