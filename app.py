import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__,template_folder = "templates")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/", methods=["POST"])
def upload():
    upload_folder = os.path.join(APP_ROOT, 'images/')
    
    print(upload_folder)
    if not os.path.isdir(upload_folder):
            os.mkdir(upload_folder)
    else:
        print("Error creating upload image directory: {}".format(upload_folder))
    
        
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
    
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "".join([upload_folder, filename])

        print ("Uploading file...:", filename)
        print ("Saving it to:", destination)
        if not os.path.isdir(destination):

            upload.save(destination)
        else:
            pass

    
    return render_template("upload.html", image_name=filename)


@app.route("/", methods=["POST"])
def clear():
    upload_folder = os.path.join(APP_ROOT, 'images/')
    for root, dirs, files in os.walk(upload_folder):
            for file in files:
                os.remove(os.path.join(root, file))

    
    return redirect('/')

   

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(port=4445, debug=True)