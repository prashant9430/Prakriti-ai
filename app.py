from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🌿 Prakriti AI is alive!"

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.json
    print(data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
