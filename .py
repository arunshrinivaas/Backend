from flask import Flask, request, jsonify
import base64

app = Flask(_name_)

def process_data_array(data):
    numbers = [item for item in data if item.isdigit() or item.isnumeric()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase = max([item for item in alphabets if item.islower()], default=None)
    return numbers, alphabets, highest_lowercase

def validate_base64_file(file_base64):
    if file_base64:
        try:
            file_data = base64.b64decode(file_base64)
            file_size_kb = len(file_data) / 1024  
            mime_type = "image/png" 
            return True, mime_type, round(file_size_kb, 2)
        except Exception as e:
            return False, None, None
    return False, None, None


@app.route('/api/data', methods=['POST'])
def process_data():

    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', '')

    numbers, alphabets, highest_lowercase = process_data_array(data)
    file_valid, file_mime_type, file_size_kb = validate_base64_file(file_b64)

   
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

 
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase,
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response), 200


@app.route('/api/operation', methods=['GET'])
def get_operation_code():
    user_id = "john_doe_17091999"  
    return jsonify({"operation_code": "OP56789", "user_id": user_id}), 200

if _name_ == '_main_':
    app.run(debug=True)
