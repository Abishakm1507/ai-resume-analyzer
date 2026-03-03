from flask import Flask, request, jsonify
from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text, preprocess_with_spacy
from utils.skill_extractor import extract_skills
from utils.scorer import calculate_ats_score, calculate_skill_gap
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
        extracted_text = extract_text_from_pdf(file_path)
        cleaned_text = clean_text(extracted_text)
        processed_text = preprocess_with_spacy(cleaned_text)
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


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    if "resume" not in request.files:
        return jsonify({"error": "Resume file required"}), 400

    file = request.files["resume"]
    job_description = request.form.get("job_description", "")

    if job_description == "":
        return jsonify({"error": "Job description required"}), 400

    file_path = "temp_resume.pdf"
    file.save(file_path)

    try:
        # Text pipeline
        extracted_text = extract_text_from_pdf(file_path)
        cleaned_text = clean_text(extracted_text)
        processed_text = preprocess_with_spacy(cleaned_text)

        # Skill detection
        skills = extract_skills(processed_text)

        # ATS + Gap analysis
        ats_score = calculate_ats_score(processed_text, job_description)
        missing_skills = calculate_skill_gap(skills, job_description)

        return jsonify({
            "ats_score": ats_score,
            "skills_detected": skills,
            "missing_skills": missing_skills
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)