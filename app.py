from flask import Flask, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("Flask is starting...")
    app.run(debug=True)