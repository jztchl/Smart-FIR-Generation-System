<p align="center">
  <img src="/logo.png" alt="Harmony Forge Logo" width="200">
</p>

# Smart FIR Generation System

## 🚀 Overview
The **Smart FIR Generation System** is an AI-powered web service designed to streamline the process of generating **First Information Reports (FIRs)**. Leveraging **computer vision, OCR, and deep learning**, this system can extract text, detect objects, and identify faces from uploaded images to automatically generate an FIR.

## ✨ Features
- 📸 **Image Processing** – Extracts text, detects objects, and recognizes faces in crime scene images.
- 🤖 **AI-powered FIR Generation** – Uses advanced AI models to analyze image data and generate FIR content.
- 🔍 **OCR (Optical Character Recognition)** – Reads text from crime scene images.
- 🧑‍🤝‍🧑 **Face Recognition** – Identifies known individuals from a database.
- 📊 **API-based System** – Easily integrates with other applications via REST APIs.

## 🏗️ Tech Stack
- **Backend:** Django, Django REST Framework
- **AI Models:** YOLOv8 (for object detection), Tesseract OCR (for text extraction), Face Recognition
- **Database:** SQLite (for development), PostgreSQL (recommended for production)
- **Storage:** Media folder for uploaded images
- **AI Agent:** Gemini for FIR text generation

## 🛠️ Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/jztchl/Smart-FIR-Generation-System.git
cd Smart-FIR-Generation-System
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### **3️⃣ Set Up the Database**
```sh
python manage.py migrate
```

### **4️⃣ Start the Django Server**
```sh
python manage.py runserver
```

### **5️⃣ Test the API**
Use **Postman** or **cURL** to test the API:
```sh
curl -X POST -F "image=@crime_scene.jpg" -F "crime_scene=Bank Robbery" http://127.0.0.1:8000/generate-fir/
```

## 🔥 API Endpoints
| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| **POST** | `/generate-fir/` | Upload an image and generate an FIR |
| **GET**  | `/generate-fir/` | Retrieve all generated FIRs |

## 📌 Environment Variables (.env)
Create a `.env` file and add:
```
GEMINI_API_KEY=your_api_key
```

## 🛡️ Security & Best Practices
- 🔒 **Use environment variables** instead of hardcoding credentials.
- 🚀 **Deploy with Gunicorn & Nginx** for production.
- 🏦 **Use PostgreSQL** instead of SQLite in production.

## 📜 License
This project is licensed under the **MIT License**.

---
💡 **Need Help?** Feel free to open an issue on GitHub or reach out! 🚀

