from flask import Flask, request

app = Flask(__name__)

last_cmd = {"cmd": ""}  # نخزن آخر أمر هنا

@app.route('/', methods=['GET'])
def index():
    return "✅ السيرفر شغال!"

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    global last_cmd
    if request.method == 'POST':
        data = request.get_json()
        print("📩 وصلك أمر:", data)
        return {"status": "ok"}
    elif request.method == 'GET':
        if request.args.get("cmd") == "1":
            return last_cmd
        return {"status": "waiting"}

@app.route('/send/<command>', methods=['GET'])
def send_command(command):
    global last_cmd
    last_cmd = {"cmd": command}
    return {"status": "sent", "cmd": command}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
