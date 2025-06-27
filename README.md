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
- **Flask** for backend development
- **HTML / CSS / JavaScript** for frontend
- **Dropzone.js** for drag-and-drop image upload

---

## 🗂️ Project Structure

```text
sports_person_classifier/
├── models/                  → Trained machine learning models
├── server/                  → Backend logic for prediction
│   ├── artifacts/           → Intermediate model/data artifacts
│   ├── opencv/              → Haarcascade or OpenCV resources
│   ├── test_images/         → Sample images for testing
│   ├── server.py            → Main Flask application
│   ├── util.py              → Helper functions
│   ├── wavelet.py           → Wavelet feature extractor
│   └── b64.txt              → Label to base64 mapping
├── UI/                      → Frontend web interface
│   ├── images/              → Frontend image assets
│   ├── app.html             → Main HTML file
│   ├── app.css              → Styling (CSS)
│   ├── app.js               → JS logic for UI
│   ├── dropzone.min.js      → Drag & drop plugin (JS)
│   └── dropzone.min.css     → Stylesheet for Dropzone
├── Script1.ipynb            → Jupyter Notebook for model training
├── .gitignore               → Git ignore file
└── README.md                → Project documentation
