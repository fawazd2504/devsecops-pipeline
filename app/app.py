from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Test App"

# Vulnérabilité volontaire: command injection (à corriger plus tard)
@app.route("/cmd")
def cmd():
    return os.popen(request.args.get("cmd")).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
