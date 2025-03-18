<h1 align="center" id="title">TripBuddy Server</h1>

<p align="center"><img src="https://socialify.git.ci/cybot-95/Trip_Buddy_Server_Repo/image?language=1&amp;name=1&amp;owner=1&amp;pattern=Formal+Invitation&amp;theme=Light" alt="project-image"></p>

<p id="description">This API is designed to recommend places using collaborative filtering and matrix factorization concept. API takes user-id and place-type preference as inputs. A Firebase database is initialized with list of places in radius of 50km of Bengaluru fetched from Google Maps API. The other collections includes users/user_credentials and ratings.</p>

<p align="center"><img src="https://img.shields.io/badge/firebase-a08021?style=for-the-badge&amp;logo=firebase&amp;logoColor=ffcd34" alt="shields"><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&amp;logo=flask&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&amp;logo=render&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&amp;logo=visual-studio-code&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&amp;logo=python&amp;logoColor=ffdd54" alt="shields"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&amp;logo=numpy&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&amp;logo=pandas&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&amp;logo=scikit-learn&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&amp;logo=git&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="shields"></p>

<h2>🚀 Demo</h2>

[https://trip-buddy-fgpq.onrender.com/](https://trip-buddy-fgpq.onrender.com/)

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Collaborative Filtering
*   Default Recommendations
*   Error Handling

<h2>🛠️ Installation Steps:</h2>

<p>1. Install Necessary Libraries</p>

```
python -r requirements.txt
```

<p>2. Create a .env file and your Firebase Credentials</p>

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

<p>3. Run the application</p>

```
python app.py
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Flask
*   Firebase
*   SciPy
*   Numpy
*   Pandas

<h2>Need Help? 🔍</h2>
For any queries contact me @ venkyndharwad95@gmail.com

<h3>Code By Cybot-95 🤖</h3>
