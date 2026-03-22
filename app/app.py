from flask import Flask, request
import os
import requests
import json

app = Flask(__name__)

SPLUNK_URL = "http://127.0.0.1:8088/services/collector/event"
SPLUNK_TOKEN = "5024ea9b-b272-46d0-ae79-893b3bd0fa61"
HEADERS = {"Authorization": f"Splunk {SPLUNK_TOKEN}"}

def send_to_splunk(message, severity="INFO"):
    payload = {
        "event": {
            "message": message,
            "severity": severity,
            "source": "devsecops_app",
            "client_ip": request.remote_addr
        },
        "sourcetype": "flask_app_logs"
    }
    try:
        requests.post(SPLUNK_URL, headers=HEADERS, data=json.dumps(payload), timeout=2)
    except:
        pass

@app.route("/")
def home():
    send_to_splunk("Accès à la page d'accueil")
    return "DevSecOps Test App"

@app.route("/cmd")
def cmd():
    cmd_param = request.args.get("cmd")
    send_to_splunk(f"ALERTE: Exécution de commande détectée: {cmd_param}", severity="CRITICAL")
    return os.popen(cmd_param).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
