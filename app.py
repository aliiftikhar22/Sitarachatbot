from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# ================================
# Chatbot Logic Function
# ================================
def get_bot_reply(user_input):
    user_input = user_input.lower()
    if "mobile" in user_input:
        return "We have Samsung, Vivo, Infinix, and more."
    elif "ac" in user_input or "air conditioner" in user_input:
        return "Our ACs start from Rs. 115,000."
    elif "fridge" in user_input or "refrigerator" in user_input:
        return "Our refrigerators start from Rs. 55,000."
    elif "washing machine" in user_input:
        return "We have top-load washing machines starting from Rs. 16,000."
    elif "oven" in user_input or "microwave" in user_input:
        return "We have microwaves starting from Rs. 17,000."
    elif "speaker" in user_input or "handsfree" in user_input:
        return "We have wireless speakers and handsfree starting from Rs. 1,000."
    elif "owner" in user_input or "who is the owner" in user_input or "shop owner" in user_input:
        return "Mian Iftikhar Ahmed is the owner of the Sitara Center. Phone number: 0322-8452672"
    elif "contact" in user_input or "number" in user_input or "phone" in user_input or "whatsapp" in user_input:
        return "For Mobile phones and accessories: 📱 0306-4575272\nHome Appliances: 📞 0323-4537911"
    elif "hello" in user_input or "hi" in user_input:
        return "Welcome to our electronics & mobile shop! How can I help you?"
    elif "mobile chahiye" in user_input or "mobiles hain" in user_input:
        return "Haan jee, humare paas Samsung, Vivo, Infinix aur ziada brands hain."
    elif "ac chahiye" in user_input or "ac hai" in user_input:
        return "Jee haan, humare AC Rs. 115,000 se start hotay hain."
    elif "fridge chahiye" in user_input or "refrigerator hai" in user_input:
        return "Fridges Rs. 55,000 se start hotay hain."
    elif "washing machine chahiye" in user_input or "machine hai" in user_input:
        return "Jee, humare paas top-load washing machines Rs. 16,000 se milti hain."
    elif "oven chahiye" in user_input or "microwave hai" in user_input:
        return "Microwave aur ovens Rs. 17,000 se start hotay hain."
    elif "speaker hai" in user_input or "handsfree chahiye" in user_input:
        return "Wireless speaker aur handsfree Rs. 1,000 se start hotay hain."
    elif "owner kaun hai" in user_input or "dukan ka malik" in user_input:
        return "Sitara Center ke malik Mian Iftikhar Ahmed hain."
    else:
        return "Please ask about mobiles, ACs, ovens, or other electronics. / Bara e meharbani, sawal mobile, fridge, ya kisi aur product ka poochein."

# ================================
# Chatbot Endpoint for Postman
# ================================
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = get_bot_reply(user_input)
    return jsonify({"reply": reply})

# ================================
# Webhook Endpoint (Facebook)
# ================================
VERIFY_TOKEN = "sitara123"
PAGE_ACCESS_TOKEN = "EAAOPI7KEnMUBOzDB0ovDf6ZBJ4mXiMDjikUQL9zCJCPMERx0E4G5I49YZCVicTZBFW7NzYhUbZBly5KV2vtdcxZAtl8ZCIijf01JGGvZBgoESbpwN2wKZC3hZBZAaO0IpCsGwzui6UhpB7erKZA5N4BFPcehUWfuNwZAdo9JbsEh1oPmokZBQEyC5bxxlObXJlHLMtIFktG1q9ACc"

def send_reply(sender_id, reply_text):
    url = f"https://graph.facebook.com/v19.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "recipient": {"id": sender_id},
        "message": {"text": reply_text}
    }
    requests.post(url, headers=headers, json=payload)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        mode = request.args.get("hub.mode")
        if token == VERIFY_TOKEN and mode == "subscribe":
            return challenge, 200
        return "Invalid verification token", 403

   elif request.method == "POST":
    data = request.get_json()
    print("Webhook data received:", data)

    try:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                print("Change value:", value)

                messages = value.get("messages", [])
                print("Messages found:", messages)

                if messages:
                    sender = messages[0]["from"]
                    text = messages[0]["text"]["body"]
                    print(f"📩 Message from {sender}: {text}")
                    reply_text = get_bot_reply(text)
                    send_reply(sender, reply_text)
    except Exception as e:
        print("Webhook error:", e)

    return "Webhook received", 200

# =====================
# Required for Render
# =====================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
