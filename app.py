from flask import Flask, request, jsonify

app = Flask(__name__)

def process_data(data):
    numbers = []
    alphabets = []
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)

    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    return numbers, alphabets, highest_lowercase

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    request_data = request.get_json()
    data = request_data.get('data', [])

    numbers, alphabets, highest_lowercase = process_data(data)

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
