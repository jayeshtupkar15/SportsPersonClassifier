
# 🏅 Sports Person Classifier 🤖📸

An end-to-end machine learning project that classifies images of famous sports personalities using image processing, scikit-learn, and a Flask-powered web interface. The model predicts one of **five iconic athletes** based on the input image.

---

## 🧠 What It Does

This project can classify a given image as one of the following sports icons:

- 🎾 Maria Sharapova  
- 🎾 Serena Williams  
- 🏏 Virat Kohli  
- 🎾 Roger Federer  
- ⚽ Lionel Messi  

Upload an image through the simple UI, and get an instant prediction powered by machine learning and OpenCV.

---

## 🚀 Technologies Used

- **Python**
- **Machine Learning (scikit-learn)**
- **OpenCV** for image processing
- **NumPy, Matplotlib, Seaborn** for preprocessing & visualization
- **Flask** (backend)
- **HTML/CSS/JavaScript** (frontend)
- **Dropzone.js** for drag-and-drop upload

---

## 🗂️ Project Structure
sports_person_classifier/
├── models/ # Trained model files
├── server/ # Backend server logic
│ ├── artifacts/
│ ├── opencv/
│ ├── test_images/
│ ├── server.py # Main Flask app
│ ├── util.py # Utility functions
│ ├── wavelet.py # Wavelet feature extraction
│ └── b64.txt # Label mappings
├── UI/ # Frontend (HTML, CSS, JS)
│ ├── images/
│ ├── app.html
│ ├── app.css
│ ├── app.js
│ ├── dropzone.min.js
│ └── dropzone.min.css
├── Script1.ipynb # Model training & evaluation
├── .gitignore
├── README.md

