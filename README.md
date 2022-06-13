# JAGA-API
Here is link github for ML-Jaga = https://github.com/fnnysalsabilaa/JAGA.git
Here is link github for MD-Jaga = https://github.com/RizaniHusyairi/JAGA.git

The API was used to deploy ML model to Google Cloud. We created it using Flask in VScode. Here is the step for it 

 1) Install the environment
```
pip install virtualenv
virtualenv <PUT YOUR ENVIRONMENT NAME >
<YOUR ENVIRONMENT NAME>\Scripts\activate.bat
python -m pip install --upgrade pip
```

 2) Install the variable
```
pip install flask
pip install numpy 
pip install pandas 
pip install lightgbm
```

 3) Input models (download the models, put in the same file as your environment) 

4) The file type for the application we are using is .pkl and the machine learning mode is LightGBM

5) Download the app.py from the repository (also put in the same file as your environment) 

6) Run the application 
```
python -m flask run
```
-----------------------------------------------------------------------------------------------------------------------------------
## DEPLOY FLASK APPLICATION IN GOOGLE CLOUD 

1) Activate Cloud Run API and Cloud Build API 
![image](https://user-images.githubusercontent.com/99376250/173269907-86600edf-f000-4fd0-a877-bab7713da1c9.png)
![image](https://user-images.githubusercontent.com/99376250/173269978-8ec97139-f044-47a1-b0ea-b3880989a27e.png)

2) Install and init Google Cloud SDK
![image](https://user-images.githubusercontent.com/99376250/173270052-8f39b86d-2c75-4063-89b5-ca36dbf08a18.png)

3) Initialize the dockerfile file and .dockerignore file in the VsCode
4) Build and Deploy the ML Flask Model
```
gcloud builds submit --tag gcr.io/<project_id>/<function_name>
gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed
```
-----------------------------------------------------------------------------------------------------------------------------------
## CONNECTING SPREADSHEET DATA TO FIREBASE 

1) Create your own Spreadsheet database 
![image](https://user-images.githubusercontent.com/99376250/173258025-ee6bf1bd-83ad-4079-980c-8143f7dc99c8.png)

2)  Hover to Extensions -> App Script 
![image](https://user-images.githubusercontent.com/99376250/173258064-9db7f4c9-1ae7-4cec-8e8f-69a9f244b79d.png)
![image](https://user-images.githubusercontent.com/99376250/173258081-52e93ea6-60f3-4571-92f4-5d9491326f93.png)

3) Input your Firebase Library by copy paste this API KEY 
```
FIREBASE_API_KEY = 1VUSl4b1r1eoNcRWotZM3e87ygkxvXltOgyDZhixqncz9lQ3MjfT1iKFw
```
4)  Install the Latest Version 
![image](https://user-images.githubusercontent.com/99376250/173258200-94a5c0fa-4db9-41b2-b506-a92dc33d92c3.png)

5)  Generate your own Private Key in Google Cloud Console (API&Services -> Credentials -> Service Accounts). 
6)  Make sure the Google Cloud Platform that you are using is the same platform that you use for Cloud Firebase
7)  Here is some of the important things that you need to look at 
```
CLIENT_EMAIL
PRIVATE_KEY
PROJECT_ID
```
8)  Implemeting the Code. Next put your credentials first, in the top of your code. 
```
function datajaga() {
const email = "PUT THE YOUR EMAIL FROM CREDENTIALS->SERVICE ACCCOUNTS -> EMAIL that was chosen for App Engine";
   const key = "PUT YOUR API KEY ";
   const projectId = "YOUR PROJECT ID ";
   var firestore = FirestoreApp.getFirestore (email, key, projectId);
 .....
 }
```
9) After putting your credentials, you could generate variabel that will be used for your function and where and how you will get the data 
```
{
...
// Mendapatkan data dari spreadsheet 
   var excel = SpreadsheetApp.getActiveSpreadsheet();
   var nama = "THE NAME OF YOUR SHEET"; 
   var data = excel.getSheetByName(nama); 

   //dapetin data
   var datacolumn = data.getLastColumn(); // kolom terakhir
   var datarow = data.getLastRow(); // row terakhir
   var datapertama = 2; // THE FIRST ROW THAT HAD THE DATA
   var rangedata = data.getRange(2,1,datarow-datapertama+1,datacolumn); // CREATING 5 COLUMN FOR THE PLACE

   // dapetin data 
   var sumberdata = rangedata.getValues();
   var panjangsumber = sumberdata.length; #ini bakal dipakai untuk looping 
...
}
```
10) Looping To get the Data and the post it as a form of RealTime Database
```
 for (var i=0;i<panjangsumber;i++){

     if(sumberdata[i][1] !== '') {
       var data = {};
       var tanggal = sumberdata[i][0].toString(); //mengubah kolom tanggal dari number jadi tipe string
       var tambahtanggal = new Date(tanggal);
       var stringdata = JSON.stringify(tambahtanggal);
       var updatetanggal = stringdata.slice(1,11);
       
        //naruh data di tempatnya sesuai dengan baris (bukan kolom)
       data.date = updatetanggal;
       data.days = sourceData[i][1];
       data.category = sourceData[i][2];
       data.adress = sourceData[i][3];
       data.x = sourceData[i][4];
       data.y = sourceData[i][5];
    
       firestore.createDocument("<NAMA REALTIMEDATABASE>",data);
     }
    
  }
  ...
  }
```

11) The output will be in form of JSON file in the RealTimeDatabase
![image](https://user-images.githubusercontent.com/99376250/173258782-864e5205-007e-4bcb-bbfb-2eaac64ea3db.png)
