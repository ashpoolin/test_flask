from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    # Get the input from the POST request
    input_string = request.json['message']

    # Create a dictionary with the input
    response = {"message": input_string}

    # Return the JSON response
    return jsonify([response])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)