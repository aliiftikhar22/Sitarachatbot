from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is your chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    reply = f"You said: {user_input}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
