from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

history = []

@app.route('/api', methods=['POST'])
def generate():
    content = request.json
    prompt = content.get('prompt')
    
    history.append(prompt)
    final_prompt = "\n".join(history)

    print("Got the data")

    data = {
        "model": "llama3",
        "prompt": final_prompt,
        "stream": False
    }

    url = "http://localhost:11434/api/generate"
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return jsonify({"response": actual_response})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
