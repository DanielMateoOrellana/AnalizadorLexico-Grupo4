from flask import Flask, request, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/', methods=['POST'])
def write_to_file():
    content = request.get_data(as_text=True)
    file_path = 'gui/assets/code_input.txt'

    with open(file_path, 'w') as file:
        file.write(content)
    return 'File written successfully'
@app.route('/reset_file', methods=['POST'])
def resetFile():
    content = request.get_data(as_text=True)
    file_path = 'gui/assets/code_output.txt'

    with open(file_path, 'w') as file:
        file.truncate()
    return 'File reset successfully'

@app.route('/get_content', methods=['GET'])
def get_content():
    file_path = 'gui/assets/code_input.txt'
    return send_file(file_path)


@app.route('/get_output_content', methods=['GET'])
def get_output_content():
    file_path = 'gui/assets/code_output.txt'
    return send_file(file_path)

@app.route('/execute_script', methods=['POST'])
def execute_script():
    try:
        subprocess.run(['python', 'analizador/main.py'])  # Reemplaza 'ruta_al_script.py' con la ruta a tu script Python
        return 'Script executed successfully'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


