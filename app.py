from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace "YOUR_API_KEY" with your actual OpenAI API key
API_KEY = "YOUR_API_KEY"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "prompt": message,
        "max_tokens": 50,  # Adjust based on your preference
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    return response.json()["choices"][0]["text"]


if __name__ == "__main__":
    app.run(debug=True)
