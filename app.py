from flask import Flask

app = Flask(__name__)

@app.route("/")
def project_start():
    return "Starting the project."