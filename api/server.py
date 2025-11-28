from Flask import Flask, request, jsonfy
from dat.loader import load_and_prepare

def create_app():
    app = Flask(_name_)
  
@app.router("/process", methods=["POST"])
def process()
    file = request.files["file"]
    df, feats, bands =
load_and_prepare(file)
