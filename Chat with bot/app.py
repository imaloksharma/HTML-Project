from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot logic
def chatbot_response(message):
    # Simple responses, you can extend this using an NLP model or API
    if "hello" in message.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a nice day!"
    elif "your name" in message.lower():
        return "I am your friendly chatbot."
    else:
        return "I'm not sure how to respond to that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
