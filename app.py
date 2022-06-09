# import library 
from flask import Flask, request
from flask_restful import Api, Resource
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

#Inisiasi object 
app = Flask(__name__)

# Inisiasi object flask_restful 
api = Api(app)

# load the pickled model and X_train
X_train = pickle.load(open('X_train.sav', 'rb')) #ini aku masih bingung x_train ini apaan, aku butuh bantuan pengalaman MLmu
model = pickle.load(open('model.pkl', 'rb'))

# feature scale data after fitting scalar object to pickled training set
sc = StandardScaler()
X_train = sc.fit_transform(X_train)

# inisiasi variabel kosong bertipe dictionary 
Resource = {} #variable global, ini udh dalam bentuk dictionary = json (berarti udh json)

#membuat class Resource 
class ContohResource(Resource):
    #method get and post 
    def get(self):
        # get request that returns the JSON format for API request
        return {"JSON data format": {"Category": 18,
                                     "DayOfWeek": 7,
                                     "Dates",
                                     "Address",
                                     "PdDistrict",
                                     "X",
                                     "Y"
                                    }
                }, 200
    def post(self):
        # post request
        # make model and X_train global variables
        global model
        global X_train #again aku gk tahu ini X_Train ini apaan 
        # it gets patient's record and returns the ML model's prediction
        data = request.get_json()

        try:
            category = int(data["Category"])
            daysofweek = object(data["DaysofWeek"])
            dates = object(data["Dates"])
            address = object(data["Address"])
            pddistrict = object(data["PdDistrict"])
            x = float(data["X"])
            y = float(data["Y"])

            # model expects a 2D array
            new_record = [[category, daysofweek, dates, address, pddistrict, x, y]]
            # feature scale the data
            scaled_data = sc.transform(new_record)
            # dictionary containing the diagnosis with the key as the model's prediction
            #aku masih bingung outputnya ini apaan TT, soalnya harusnya pake Google Maps API gitu kalau mau digabungin sama MLnya  
            #a = pd.DataFrame()
            #for i, index in enumerate(out):
            #a.loc[i, 'Subject'] = df_news['Subject'][index]
            #diagnosis.loc[c['Hasil Prediksi'] == c['Category'] , 'Keterangan'] = 'True'
            # pass scaled data to model for prediction
            new_pred = model.predict(scaled_data)[0]
            # get corresponding value from the diagnosis dictionary (using the model prediction as the key)
            result = diagnosis.get(new_pred)
            return {'Diagnosis': result}, 200
        except:
            # if client sends the wrong request or data type then return correct format
            return {'Error! Please use this JSON format': {"Category": 18,
                                              "DayOfWeek": 7,
                                              "Dates",
                                              "Address",
                                              "PdDistrict",
                                              "X",
                                              "Y"
                                             }}, 500
      
#CATATAN : DIR ABIS INI KAMU TAMBAHIN YANG BARU INI KAMU JALANIN ULANG YA <3

#setup resourcenya 
api.add_resource(ContohResource, "/Jaga", methods=["GET", "POST"]) #adira bagian ini kamu copy ulang ya hwhwhw, nambahin "POST"

if __name__== "__main__": 
    app.run(debug=True, port=5005)

