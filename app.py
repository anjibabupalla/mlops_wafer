from flask import Flask, render_template, request, json,jsonify
import os
from flask.wrappers import Response
import yaml
import joblib
import numpy as np


params_path = "config/params.yaml"
webapp_root = "webapp"
static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")
from src.get_data import read_params

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":str(response)}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again later!"}        
        return error






@app.route("/", methods={"GET", "POST"})
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template('index.html',response=response)
            elif request.json:
                response = api_response(request)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}
            return render_template("404.html",error=e)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
