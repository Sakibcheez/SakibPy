from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        marks = int(user_message)  # user gives marks
        prediction = model.predict([[marks]])[0]
        bot_reply = "✅ Pass!" if prediction == 1 else "❌ Fail!"
    except:
        bot_reply = "Please enter a number (marks)."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
