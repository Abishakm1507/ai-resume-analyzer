from flask import Flask, request, jsonify
from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text, preprocess_with_spacy
from utils.skill_extractor import extract_skills
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Resume Analyzer Backend Running 🚀"


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_path = "temp_resume.pdf"
    file.save(file_path)

    try:
        # 1️⃣ Extract text
        extracted_text = extract_text_from_pdf(file_path)

        # 2️⃣ Clean text
        cleaned_text = clean_text(extracted_text)

        # 3️⃣ NLP processing
        processed_text = preprocess_with_spacy(cleaned_text)

        # 4️⃣ Skill extraction
        skills = extract_skills(processed_text)

        return jsonify({
            "extracted_preview": extracted_text[:200],
            "cleaned_preview": cleaned_text[:200],
            "processed_preview": processed_text[:200],
            "skills_detected": skills
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)