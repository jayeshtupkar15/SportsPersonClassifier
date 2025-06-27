import os
from flask import Flask, send_from_directory, request, jsonify
import util  # your existing util module

app = Flask(__name__)

# Set the absolute path to your UI folder (adjust if your folder structure is different)
UI_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'UI'))

@app.route('/')
def serve_homepage():
    return send_from_directory(UI_FOLDER, 'app.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(UI_FOLDER, path)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    result = util.classify_image(image_data)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5000)
