from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'


def sort_and_pair_images(file_list):
    # Split files into questions and answers
    questions = sorted([f for f in file_list if "Question" in f])
    answers = sorted([f for f in file_list if "Answer" in f])

    # Pairing questions and answers
    paired_images = []
    for question in questions:
        # Extract the number from the question file name
        number = ''.join(filter(str.isdigit, question))
        # Find the corresponding answer
        answer = next((a for a in answers if number in a), None)
        if answer:
            paired_images.append((question, answer))

    return paired_images

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'files[]' not in request.files:
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('display_images'))
    return render_template('upload.html')

@app.route('/display', methods=['GET'])
def display_images():
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    file_list = [os.path.join(app.config['UPLOAD_FOLDER'], file) for file in file_list]
    sorted_pairs = sort_and_pair_images(file_list)
    return render_template('display.html', sorted_pairs=sorted_pairs)

if __name__ == '__main__':
    app.run(debug=True)
