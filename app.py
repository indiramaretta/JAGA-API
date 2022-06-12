from flask import Flask
from flask import request
import pandas as pd
import lightgbm as lgb
import numpy as np
import json
import string
import random

# Load the model
lgbModel = lgb.Booster(model_file="Crime Prediction/model/lgb_gbdt5.pkl")
#jangan lupa buat path untuk folder file pkl

app = Flask(__name__)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return 'Refreshable Key: ' + ''.join(random.choice(chars) for _ in range(size))

def fixDF(data):
    data = data.astype({
          'LotArea':int
        , 'Neighborhood':'category'
        , 'Condition1':'category'
        , 'Condition2':'category'
        , 'OverallQual':int
        , 'OverallCond':int
        , 'YearBuilt':int
        , 'SaleCondition':'category'
    })
    return data

@app.route("/jaga", methods = ['GET','POST'])
def user():
    if request.method == 'GET':
        # Exists solely to make sure the running service has updated
        return id_generator()

    if request.method == 'POST':
        df = fixDF(pd.DataFrame.from_dict(request.get_json(), orient='index').T.infer_objects())
        pred = np.round(lgbModel.predict(df),2)
        response = json.dumps({'Category': pred[0]})

        return response

if __name__== "__main__": 
    app.run(debug=True, port=5005)

