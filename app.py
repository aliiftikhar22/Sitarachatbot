from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# ================================
# Chatbot Endpoint for App/Postman
# ================================
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "mobile" in user_input:
        return jsonify({"reply": "We have Samsung, Vivo, Infinix, and more."})
    elif "ac" in user_input or "air conditioner" in user_input:
        return jsonify({"reply": "Our ACs start from Rs. 115,000."})
    elif "fridge" in user_input or "refrigerator" in user_input:
        return jsonify({"reply": "Our refrigerators start from Rs. 55,000."})
    elif "washing machine" in user_input:
        return jsonify({"reply": "We have top-load washing machines starting from Rs. 16,000."})
    elif "oven" in user_input or "microwave" in user_input:
        return jsonify({"reply": "We have microwaves starting from Rs. 17,000."})
    elif "speaker" in user_input or "handsfree" in user_input:
        return jsonify({"reply": "We have wireless speakers and handsfree starting from Rs. 1,000."})
    elif "owner" in user_input or "who is the owner" in user_input or "shop owner" in user_input:
        return jsonify({"reply": "Mian Iftikhar Ahmed is the owner of the Sitara Center."})
    elif "hello" in user_input or "hi" in user_input:
        return jsonify({"reply": "Welcome to our electronics & mobile shop! How can I help you?"})

    # Urdu support
    elif "mobile chahiye" in user_input or "mobiles hain" in user_input:
        return jsonify({"reply": "Haan jee, humare paas Samsung, Vivo, Infinix aur ziada brands hain."})
    elif "ac chahiye" in user_input or "ac hai" in user_input:
        return jsonify({"reply": "Jee haan, humare AC Rs. 115,000 se start hotay hain."})
    elif "fridge chahiye" in user_input or "refrigerator hai" in user_input:
        return jsonify({"reply": "Fridges Rs. 55,000 se start hotay hain."})
    elif "washing machine chahiye" in user_input or "machine hai" in user_input:
        return jsonify({"reply": "Jee, humare paas top-load washing machines Rs. 16,000 se milti hain."})
    elif "oven chahiye" in user_input or "microwave hai" in user_input:
        return jsonify({"reply": "Microwave aur ovens Rs. 17,000 se start hotay hain."})
    elif "speaker hai" in user_input or "handsfree chahiye" in user_input:
        return jsonify({"reply": "Wireless speaker aur handsfree Rs. 1,000 se start hotay hain."})
    elif "owner kaun hai" in user_input or "dukan ka malik" in user_input:
        return jsonify({"reply": "Sitara Center ke malik Mian Iftikhar Ahmed hain."})

    else:
        return jsonify({"reply": "Please ask about mobiles, ACs, ovens, or other electronics. / Bara e meharbani, sawal mobile, fridge, ya kisi aur product ka poochein."})

# ============================
# Webhook Endpoint (GET/POST)
# ============================
VERIFY_TOKEN = "sitara123"  

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Facebook/Meta webhook verification
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        mode = request.args.get("hub.mode")

        if token == VERIFY_TOKEN and mode == "subscribe":
            return challenge, 200
        return "Invalid verification token", 403

    elif request.method == "POST":
        data = request.get_json()
        print("Webhook data received:", data)

        # Example: handle incoming messages from WhatsApp or Messenger
        try:
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    messages = value.get("messages")
                    if messages:
                        sender = messages[0]["from"]
                        text = messages[0]["text"]["body"]
                        print(f"Message from {sender}: {text}")
        except Exception as e:
            print("Webhook error:", e)

        return "Webhook received", 200

# =====================
# Required for Render
# =====================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
