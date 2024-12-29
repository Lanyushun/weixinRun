from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/update_steps', methods=['POST'])
def update_steps():
    data = request.json
    account = data.get('account')
    password = data.get('password')
    steps = data.get('steps')

    if not account or not password or not steps:
        return jsonify({'error': 'Missing parameters'}), 400

    api_url = f'https://steps.api.030101.xyz/api?account={account}&password={password}&steps={steps}'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return jsonify({'message': 'Steps updated successfully', 'response': response.json()})
        else:
            return jsonify({'error': 'Failed to update steps', 'details': response.text}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

@app.route('/')
def home():
    return "Flask Server is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
