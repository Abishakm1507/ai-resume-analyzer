# 🚀 AI Resume Analyzer

An AI-powered Resume Analyzer that evaluates resume relevance against a job description using NLP and Machine Learning techniques.

This system simulates how Applicant Tracking Systems (ATS) rank resumes and provides actionable insights to improve alignment with job roles.

---

## 🔍 Features

- 📄 Upload Resume (PDF)
- 🧠 NLP-based Text Preprocessing (spaCy)
- 📊 ATS Score Calculation (TF-IDF + Cosine Similarity)
- 📈 Skill Match Percentage
- ⚠ Missing Skill Detection
- 💡 Smart Resume Improvement Suggestions
- 🎨 Modern React + Tailwind UI
- ⚙ REST API Integration (Flask Backend)

---

## 🏗 System Architecture

![system architecture](https://ik.imagekit.io/ulajgq5pme/ChatGPT%20Image%20Mar%203,%202026,%2011_29_30%20PM.png)

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- spaCy
- Scikit-learn
- PyMuPDF
- Flask-CORS

### Frontend
- React.js
- Axios
- Tailwind CSS

---

## 🧠 Machine Learning Logic

The ATS score is calculated using:

- **TF-IDF Vectorization**
- **Cosine Similarity**

This measures semantic similarity between:
- Resume content
- Job description

Skill match percentage is calculated by comparing detected resume skills with job description requirements.

---

## 📂 Project Structure
```bash
ai-resume-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── services/
│   │   │   ├── pdf_service.py
│   │   │   ├── nlp_service.py
│   │   │   ├── skill_service.py
│   │   │   └── scoring_service.py
│   │   └── config.py
│   │
│   ├── run.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadForm.js
│   │   │   ├── ResultCard.js
│   │   │   └── ProgressBar.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
├── README.md
└── .gitignore
```

---

## 🎯 Why This Project Matters

This project demonstrates:

- Applied NLP techniques
- Feature engineering
- Machine Learning similarity modeling
- Backend API design
- Full-stack integration
- Real-world problem solving

It simulates real-world ATS systems used by companies during resume screening.

---

## 🚀 Future Improvements

- GPT-powered resume rewriting suggestions
- Role-specific skill database expansion
- Advanced semantic matching using sentence transformers
- PDF report download
- Authentication & user history tracking
- Cloud deployment with CI/CD
