from flask import Flask, json, render_template,request, jsonify
from lxml import html
import os
from flask_cors import CORS
from werkzeug.utils import secure_filename
import glob

UPLOAD_FOLDER = '/home/diana/Documentos/extension_chrome/static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def print():
    from main import print
    #return print()
    x =  print()
    return render_template("index.html",x = x)


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        files = glob.glob('static/uploads/*')
        for f in files:
            os.remove(f)
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        #return 'UPLOAD COM SUCESSO', 200
        return render_template("executa_file.html")

    if request.method == 'GET':
        #return render_template("index.html",x = x)
        return jsonify("Upload com sucesso!!")
    
@app.route('/test', methods=['POST','GET'])
def prints():
    resultado="ola"
    return jsonify(resultado)

@app.route('/web_image', methods=['GET', 'POST'])
def web():

    req = request.get_json()
    
    url = req['site'].replace("'", "")
    url = req['site'].replace('"', "")

    from imagens import main
    result = main(url)
    
    if request.method == 'GET':
        #return render_template("index.html",x = x)
        return jsonify(result) 
         # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        #print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/execute', methods=['GET', 'POST'])
def execute():

    from num_files import arr
    from execute_upload import ex

    resultado = ex()
    x = arr()

    if request.method == 'GET':
        #return render_template("index.html",x = x)
        return jsonify(x,resultado)  
    # POST request
    if request.method == 'POST':
        print(request.get_json())  
        return 'Sucesss', 200

@app.route('/execute_web', methods=['GET', 'POST'])
def execute_web():

    from num_files import arr_web
    from execute_web import ex

    resultado = ex()
    x = arr_web()

    if request.method == 'GET':
        #return render_template("index.html",x = x)
        return jsonify(x,resultado)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == "__main__":
    #app.run(ssl_context='adhoc')
    app.run()
