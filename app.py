from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "BOT ONLINE"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("SINAL:", data)

    if data and data.get("signal") == "BUY":
        print("COMPRA")
    elif data and data.get("signal") == "SELL":
        print("VENDA")

    return "OK"

app.run(host="0.0.0.0", port=5000)
