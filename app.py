# import library 
from codecs import namereplace_errors
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#Inisiasi object 
app = Flask(__name__)

# Inisiasi object flask_restful 
api = Api(app)

# inisiasi object flask coRS
CORS(app)

# inisiasi variabel kosong bertipe dictionary 
identitas = {} #variable global, ini udh dalam bentuk dictionary = json (berarti udh json)

#membuat class Resource 
class ContohResource(Resource):
    #method get and post 
    def get(self): 
        
        #response = {"msg": "Hallo dunia, ini app restful pertamaku"}
        return identitas

    def post(self): 
        nama = request.form["nama"] 
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response 

#CATATAN : DIR ABIS INI KAMU TAMBAHIN YANG BARU INI KAMU JALANIN ULANG YA <3

#setup resourcenya 
api.add_resource(ContohResource, "/api", methods=["GET", "POST"]) #adira bagian ini kamu copy ulang ya hwhwhw, nambahin "POST"

if __name__== "__main__": 
    app.run(debug=True, port=5005)

