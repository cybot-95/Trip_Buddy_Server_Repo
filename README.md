<h1 align="center" id="title">TripBuddy Server</h1>

<p align="center"><img src="https://socialify.git.ci/cybot-95/Trip_Buddy_Server_Repo/image?language=1&amp;name=1&amp;owner=1&amp;pattern=Formal+Invitation&amp;theme=Light" alt="project-image"></p>

<p id="description">This API is designed to recommend places using collaborative filtering and matrix factorization concept. API takes user-id and place-type preference as inputs. A Firebase database is initialized with list of places in radius of 50km of Bengaluru fetched from Google Maps API. The other collections includes users/user_credentials and ratings.</p>

<p align="center"><img src="https://img.shields.io/badge/firebase-a08021?style=for-the-badge&amp;logo=firebase&amp;logoColor=ffcd34" alt="shields"><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&amp;logo=flask&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&amp;logo=render&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&amp;logo=visual-studio-code&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&amp;logo=python&amp;logoColor=ffdd54" alt="shields"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&amp;logo=numpy&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&amp;logo=pandas&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&amp;logo=scikit-learn&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&amp;logo=git&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="shields"></p>

<h2>🚀 Demo</h2>

Check out the working web application here: [https://trip-buddy-fgpq.onrender.com/](https://trip-buddy-fgpq.onrender.com/)

  
  
<h2>🌟 Features</h2>

Here're some of the project's best features:

✔️   Collaborative Filtering <br>
✔️   Default Recommendations <br>
✔️   Error Handling <br>
✔️   API Health Check <br>
✔️   Update Data and Re-Train <br>

<h2>🖇️ Pre-requesities </h2>

1️⃣ Setup your Firebase, visit [Google Firebase](https://console.firebase.google.com/). Make a new collection under your desired name.

2️⃣ Generate a your Firebase Private Key(.JSON File), refer this [How to get my Firebase Service Account Key file](https://clemfournier.medium.com/how-to-get-my-firebase-service-account-key-file-f0ec97a21620) by Medium.

3️⃣ Setup Google Maps API and obtain API key. Refer this [How to create a Google Maps API Key](https://webbuildersgroup.com/blog/how-to-create-a-google-maps-api-key) by Webbuilders.


<h2>⚙️ Installation and Setup:</h2>

<p>1️⃣ Install Necessary Libraries</p>

```
python -r requirements.txt
```

<p>2️⃣ Create a new folder <b>Key</b> and store your Firebase key file here.The file should look like this.</p>

```
{
  "type": "service_account",
  "project_id": "YOUR_PROJECT_ID",
  "private_key_id": "YOUR_PROJECT_KEY_ID",
  "private_key": "YOUR_KEY_HERE",
  "client_email": "firebase-adminsdk-fbsvc@YOUR-PROJECT-NAME.iam.gserviceaccount.com",
  "client_id": "YOUR_CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40YOUR_PROJECT_NAME.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

<p>3️⃣ Create a .env file in root folder and store <b>Google Maps API Key</b></p>

```
GOOGLE_MAPS_API_KEY = "YOUR MAPS API KEY HERE"
```

<p>4️⃣ Fetch places from the <b>Google Maps API</b> and display them.</p>

```
cd Places
python places_fetch.py
python places_display.py
```
<p>5️⃣ Generate </b>Users and their <b>Credentials</b>.</p>

```
cd Users
python generate_users.py
python user_credentials.py
```

<p>6️⃣ Generate ratings, this fetches users and places and generates random <b>Ratings</b> for places from each user.</p>

```
python generate_ratings.py
```

<p>7️⃣ Visit Firebase and verify the entries.</p>

<p>8️⃣ Train and save the model</p>

```
cd Train
python place_reco_train.py
```

<p>9️⃣ Deploy the model on local host using <b>Flask</b>.</p>

```
python app.py
```
The app will be deployed on your localhost on Port 5000 by default.


<h2>⛳ Verify The Run</h2>  

🔹Visit <b>Postman</b> or hit up your favourite browser and type,
[http://127.0.0.1:5000/recommend?place_type=tourist_attraction&uid=100](http://127.0.0.1:5000/recommend?place_type=tourist_attraction&uid=100)

⚠️ If ```place_type``` &  ```uid``` is not set then the app will throw default recommendation. Default value of ```place_type``` & ```uid``` is set to ```None```.  

<h2> <b> 📁 Technology Stack </b> </h2>

*   <b>Language & Runtime:</b> Python
*   <b>Framework</b> Flask
*   <b>Data Processing and Model:</b> Scikit-Learn, Pandas, NumPy
*   <b>Database & Storage:</b> Firebase Firestore
*   <b>APIs:</b> Google Maps API
*   <b>Utilities:</b> Flask-CORS

<h2>🔍 Need Help?</h2>

Contact me here 📧, [Venky Dharwad](mailto:venkyndharwad95@gmail.com?subject=[GitHub%20Trip%20Buddy]%20Source%20Han%20Sans) 

<h3>Code By Cybot-95 🤖</h3>
