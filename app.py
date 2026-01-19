import os
from flask import Flask, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# 🔹 Webhook verification
@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid token"

# 🔹 Receive message
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = msg["from"]
        text = msg["text"]["body"]

        send_message(sender, f"🌿 Hi! Main Prakriti AI hoon 🤖\nTumne likha: {text}")

    except:
        pass

    return "ok"

# 🔹 Send message function
def send_message(to, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "PRAKRITI-AI_VERIFY"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Invalid token", 403

    if request.method == "POST":
        data = request.json
        print("Incoming message:", data)
        return "EVENT_RECEIVED", 200
