from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
from model.model_loader import run_drs_cam

UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result_path = run_drs_cam(filepath)
        result_filename = os.path.basename(result_path)
        result_image_url = url_for('static', filename=f'outputs/{result_filename}')

        return render_template('result.html', result_image=result_image_url)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
