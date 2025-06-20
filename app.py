from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    if "mobile" in user_message:
        return jsonify({"reply": "We have Samsung, Vivo, Infinix, and more."})
    elif "ac" in user_message or "air conditioner" in user_message:
        return jsonify({"reply": "Our ACs start from Rs. 115,000."})
    elif "fridge" in user_message or "refrigerator" in user_message:
        return jsonify({"reply": "Our refrigerators start from Rs. 55,000."})
    elif "washing machine" in user_message:
        return jsonify({"reply": "We have top-load washing machines starting from Rs. 16,000."})
    elif "oven" in user_message or "microwave" in user_message:
        return jsonify({"reply": "We have microwaves starting from Rs. 17,000."})
    elif "speaker" in user_message or "handsfree" in user_message:
        return jsonify({"reply": "We have wireless speakers and handsfree starting from Rs. 1,000."})
    elif "owner" in user_message or "who is the owner" in user_message or "shop owner" in user_message:
        return jsonify({"reply": "Mian Iftikhar Ahmed is the owner of the Sitara Center."})
    elif "hello" in user_message or "hi" in user_message:
        return jsonify({"reply": "Welcome to our electronics & mobile shop! How can I help you?"})

    # Urdu language support
    elif "mobile chahiye" in user_message or "mobiles hain" in user_message:
        return jsonify({"reply": "Haan jee, humare paas Samsung, Vivo, Infinix aur ziada brands hain."})
    elif "ac chahiye" in user_message or "ac hai" in user_message:
        return jsonify({"reply": "Jee haan, humare AC Rs. 115,000 se start hotay hain."})
    elif "fridge chahiye" in user_message or "refrigerator hai" in user_message:
        return jsonify({"reply": "Fridges Rs. 55,000 se start hotay hain."})
    elif "washing machine chahiye" in user_message or "machine hai" in user_message:
        return jsonify({"reply": "Jee, humare paas top-load washing machines Rs. 16,000 se milti hain."})
    elif "oven chahiye" in user_message or "microwave hai" in user_message:
        return jsonify({"reply": "Microwave aur ovens Rs. 17,000 se start hotay hain."})
    elif "speaker hai" in user_message or "handsfree chahiye" in user_message:
        return jsonify({"reply": "Wireless speaker aur handsfree Rs. 1,000 se start hotay hain."})
    elif "owner kaun hai" in user_message or "dukan ka malik" in user_message:
        return jsonify({"reply": "Sitara Center ke malik Mian Iftikhar Ahmed hain."})
    
    else:
        return jsonify({"reply": "Please ask about mobiles, ACs, ovens, or other electronics. / Bara e meharbani, sawal mobile, fridge, ya kisi aur product ka poochein."})

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
