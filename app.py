from flask import Flask
from flask import request
import lightgbm as lgb
import numpy as np
import pandas as pd
import json
import string
import random

lgbModel = lgb.Booster(model_file="models/LGBmodel.txt")
#jangan lupa buat path untuk folder file pkl

app = Flask(__name__)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return 'Jaga API'

def dapet(data):
    data = data.astype({
         'Dates':int
    })
    return data

@app.route("/jaga", methods = ['GET','POST'])
def user():
    if request.method == 'GET':
        return id_generator()

    if request.method == 'POST':
        df = dapet(pd.DataFrame.from_dict(request.get_json(), orient='index').T.infer_objects())
        pred = np(lgbModel.predict(df))
        response = json.dumps({'Category': pred[0]})

        return response

if __name__== "__main__": 
    app.run(debug=True, port=5005)