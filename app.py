from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to extract numbers and alphabets and find the highest lowercase alphabet
def process_data(data):
    numbers = []
    alphabets = []
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)

    # Find the highest lowercase alphabet
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    return numbers, alphabets, highest_lowercase

# POST endpoint
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    request_data = request.get_json()
    data = request_data.get('data', [])

    numbers, alphabets, highest_lowercase = process_data(data)

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your actual format
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase
    }
    return jsonify(response)

# GET endpoint
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
