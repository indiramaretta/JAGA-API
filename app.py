from flask import Flask
from flask import request
import pandas as pd
import lightgbm as lgb
import numpy as np
import json
import string
import random

# Load the model
lgbModel = lgb.Booster(model_file="Storage/models/lgbModel")

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return 'Refreshable Key: ' + ''.join(random.choice(chars) for _ in range(size))

def fixDF(datf):
    datf = datf.astype({
          'LotArea':int
        , 'Neighborhood':'category'
        , 'Condition1':'category'
        , 'Condition2':'category'
        , 'OverallQual':int
        , 'OverallCond':int
        , 'YearBuilt':int
        , 'SaleCondition':'category'
    })
    return datf

@app.route("/", methods = ['GET','POST'])
def user():
    if request.method == 'GET':
        # Exists solely to make sure the running service has updated
        return id_generator()

    if request.method == 'POST':
        df = fixDF(pd.DataFrame.from_dict(request.get_json(), orient='index').T.infer_objects())
        pred = np.round(lgbModel.predict(df),2)
        response = json.dumps({'SalePrice': pred[0]})

        return response

@app.route("/shutdown", methods = ['GET','POST'])
def shutdown():
    shutdown_server()
    return 'Server Shutting Down'


if __name__ == '__main__':
    app.run()
      
#CATATAN : DIR ABIS INI KAMU TAMBAHIN YANG BARU INI KAMU JALANIN ULANG YA <3

#setup resourcenya 
api.add_resource(ContohResource, "/Jaga", methods=["GET", "POST"]) #adira bagian ini kamu copy ulang ya hwhwhw, nambahin "POST"

if __name__== "__main__": 
    app.run(debug=True, port=5005)

