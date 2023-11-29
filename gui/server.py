from flask import Flask, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/', methods=['POST'])
def write_to_file():
    content = request.get_data(as_text=True)
    file_path = 'assets/code_input.txt'

    with open(file_path, 'w') as file:
        file.write(content)
    
    return 'File written successfully'
def write_to_output_file():
    content = request.get_data(as_text=True)
    file_path = 'assets/code_output.txt'

    with open(file_path, 'w') as file:
        file.write(content)
    
    return 'File written successfully'

@app.route('/get_content', methods=['GET'])
def get_content():
    file_path = 'assets/code_input.txt'
    return send_file(file_path)

def get_output_content():
    file_path = 'assets/code_output.txt'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
