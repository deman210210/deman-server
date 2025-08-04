from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "✅ السيرفر شغال!"

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    print("📩 وصلك أمر:", data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



