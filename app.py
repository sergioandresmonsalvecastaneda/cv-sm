from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def index():
    #return "Hello Clase Funcionó!"
    return render_template("index.html")

@app.route('/cv')
def cv():
    path = 'static/cv/Sergio_Monsalve_cv.pdf'
    return send_file(path, as_attachment=True)