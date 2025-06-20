from flask import Flask, render_template, request
import uuid, os, json
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/akshatgupta111/Documents/PYTHON PROJECTS/ReelerAI/user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        
        file_keys = request.files.keys()
        received_id = request.form.get("uuid")
        received_prompt = request.form.get("text")
        for key,val in request.files.items():
            print(f"{key} : {val}")
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                

    return render_template("create.html", myid = myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug = True)