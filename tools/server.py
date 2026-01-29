from flask import Flask, request, jsonify, send_from_directory
import os
from generator import generate_test_cases

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('user_input', '')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    result = generate_test_cases(user_input)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Server running on http://localhost:5000")
    app.run(debug=True, port=5000, host='0.0.0.0')
